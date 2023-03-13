from .spelling_history import (get_word_action_list, get_student_last_word_action, SpellingActionData, SpellingAttemptData,
                               max_actions_attempted, max_consec_times_rule_violated, add_student_action, add_student_attempt, get_word_proficiency, update_word_proficiency)
from .determine_spelling_violation import get_rule_by_id
from .utils import decapitalize_first_letter


def determine_feedback(violated_rule, student_age=10, attempts_history={}):
    feedback = ""

    if violated_rule == None:
        feedback = "That is correct!"
    elif violated_rule.id == -1:
        feedback = "Please sound out the word and try again."
    else:
        feedback = violated_rule.definition

    return feedback


def process_corrective_feedback(session_id, spelling_word, attempted_spelling, violated_rules, student_id, student_age=10, student_action_history=[]):
    feedback = ""

    curr_word_action = SpellingActionData(spelling_word, attempted_spelling)

    if violated_rules == [None]:
        curr_word_action.spelled_correctly = True
    else:
        curr_word_action.num_violated_rules = len(violated_rules)
        violated_rules_ids = []
        for rule in violated_rules:
            violated_rules_ids.append(rule.id)
        curr_word_action.violated_rules_ids = violated_rules_ids

    main_violated_rule_id = None

    word_attempt_history = get_word_action_list(student_id, spelling_word)

    last_word_action = get_student_last_word_action(student_id, spelling_word)

    if last_word_action == None:
        curr_word_action.actions_attempted = 1
        if not curr_word_action.spelled_correctly:
            main_violated_rule_id = curr_word_action.violated_rules_ids[0]
    else:
        curr_word_action.actions_attempted = last_word_action.actions_attempted + 1
        curr_word_action.max_violated_rules = max(
            last_word_action.max_violated_rules, curr_word_action.num_violated_rules)
        if not curr_word_action.spelled_correctly:
            if last_word_action.main_violated_rule_id in curr_word_action.violated_rules_ids:
                main_violated_rule_id = last_word_action.main_violated_rule_id
            else:
                main_violated_rule_id = curr_word_action.violated_rules_ids[0]

    curr_word_action.main_violated_rule_id = main_violated_rule_id

    # check for consecutive violated rules
    if last_word_action == None:
        curr_word_action.consec_times_rule_violated = 1
    else:
        if curr_word_action.main_violated_rule_id == last_word_action.main_violated_rule_id:
            curr_word_action.consec_times_rule_violated = last_word_action.consec_times_rule_violated + 1
        else:
            curr_word_action.consec_times_rule_violated = 1

    # if violated rule is due to them not paying attention
    #   do not count attempt

    # if rule violated once, twice or thrice, generate stuff
    rule_violated_count = curr_word_action.consec_times_rule_violated
    if not curr_word_action.spelled_correctly:
        if rule_violated_count == 1:
            feedback = generate_incorrect_feedback(
                curr_word_action.main_violated_rule_id, rule_violated_count)
            pass  # generate feedback with basic rule definition
        elif rule_violated_count == 2:
            feedback = generate_incorrect_feedback(
                curr_word_action.main_violated_rule_id, rule_violated_count)
            pass  # generate feedback with alternative definition if possible
        elif rule_violated_count == 3:
            feedback = generate_hint_feedback(
                curr_word_action.main_violated_rule_id, rule_violated_count)
            pass  # generate feedback with rule hint if available or alternative definition

    # if rule violated more than consec limit, just give answer should be true
    # stop processing after they get same rule wrong too many times in sequence
    if curr_word_action.consec_times_rule_violated > max_consec_times_rule_violated:
        feedback = generate_answer_feedback(
            spelling_word, curr_word_action.main_violated_rule_id)
        curr_word_action.just_give_answer = True

    # If multiple rules previously violated and less rules violated this time (started at like 3-4 but only 1 now): 	Give hopeful feedback.
    if last_word_action != None:
        less_rule_violations_now = curr_word_action.num_violated_rules < last_word_action.num_violated_rules
        if less_rule_violations_now:
            feedback = generate_hopeful_feedback(
                curr_word_action.main_violated_rule_id)

    # if word misspelled more than limit, just give answer should also be true
    # stop processing after they get same word wrong too many times in this attempt
    if curr_word_action.actions_attempted > max_actions_attempted:
        feedback = generate_answer_feedback(spelling_word)
        curr_word_action.just_give_answer = True

    # if last word was flagged as just give answer, be it the same here
    if last_word_action != None and last_word_action.just_give_answer:
        feedback = generate_answer_feedback(spelling_word)
        curr_word_action.just_give_answer = True

    if curr_word_action.spelled_correctly:
        # If word flagged as “just give answer” and correct spelling:
        # Give confirmation response. e.g. “That’s correct. No worries, you’re still learning!”
        if curr_word_action.just_give_answer:
            if last_word_action != None and last_word_action.spelled_correctly:
                feedback = generate_correct_feedback()
            else:
                feedback = generate_confirmation_feedback()
        # elif
        # calculate_proficiency()

    # record word attempt when:
    # - first attempt is correct right away
    # - first time "just give answer" becomes true for that word and session
    # - finally correct after certain number of tries
    attempt_score = None
    if not curr_word_action.recorded_attempt:
        if curr_word_action.spelled_correctly:
            attempt_score = record_word_attempt(session_id, student_id, spelling_word, curr_word_action.actions_attempted,
                                                curr_word_action.spelled_correctly)  # correct right away or finally got correct
            curr_word_action.recorded_attempt = True
        elif last_word_action != None and curr_word_action.just_give_answer and not last_word_action.just_give_answer:
            attempt_score = record_word_attempt(session_id, student_id, spelling_word, curr_word_action.actions_attempted,
                                                curr_word_action.spelled_correctly)  # first time just give answer is true
            curr_word_action.recorded_attempt = True

    # if previous action was not "just give answer", add to history
    if last_word_action == None or (last_word_action != None and not last_word_action.just_give_answer):
        add_student_action(student_id, curr_word_action)

    # TODO If proficiency for this word is low, and got higher, upon correct spelling:
        # Give congratulatory response: e.g. “Excellent! You’re getting better at this word!”
    attempt_recorded = attempt_score != None
    if attempt_score:
        # first get old proficiency
        old_proficiency = get_word_proficiency(student_id, spelling_word)
        new_proficiency = update_word_proficiency(
            student_id, spelling_word, attempt_score)

        print("Old prof:", old_proficiency, "New prof:", new_proficiency)

        if old_proficiency != -1 and new_proficiency > old_proficiency and curr_word_action.spelled_correctly:
            feedback = generate_congratulatory_feedback()

    if curr_word_action.spelled_correctly and not feedback:
        feedback = generate_correct_feedback()

    # check for undetected rules
    if violated_rules == [-1]:
        feedback = generate_unknown_feedback()

    print("Feedback at end of generate -", feedback)
    print(curr_word_action)
    return feedback


def record_word_attempt(session_id, student_id, spelling_word, actions_attempted, spelled_correctly) -> int:
    attempt_data = SpellingAttemptData(session_id, spelling_word, min(
        max_actions_attempted, actions_attempted), spelled_correctly)
    if not add_student_attempt(session_id, student_id, attempt_data):
        return None

    attempt_score = attempt_data.attempt_score

    return attempt_score


correct_feedbacks = [
    "Nice work!",
    "Awesome!",
    "Excellent!",
    "You've got this!",
    "You're doing great!",
    "That's correct!",
    "Correct!"
]

congratulatory_feedbacks = [
    "You're getting better at this word!",
    "You are improving!"
]

hopeful_feedbacks = [
    "Almost there!",
]

confirmation_feedbacks = [
    "You're still learning!",
    "Learning is a process!"
]

incorrect_feedbacks = [
    "Not quite.",
    "That's not it."
]


def generate_correct_feedback():
    print("Within generate_correct_feedback() function")
    # e.g. "Correct"
    return correct_feedbacks[0]


def generate_congratulatory_feedback():
    print("Within generate_congratulatory_feedback() function")
    # e.g. “Excellent! You’re getting better at this word!”
    return correct_feedbacks[1] + " " + congratulatory_feedbacks[0]


def generate_confirmation_feedback():
    print("Within generate_confirmation_feedback() function")
    # e.g. “That’s correct. No worries, you’re still learning!”
    return correct_feedbacks[2] + " " + confirmation_feedbacks[0]


def generate_hopeful_feedback(rule_id):
    print("Within generate_hopeful_feedback() function")
    rule = None if not rule_id else get_rule_by_id(rule_id)
    definition = None if not rule else rule.definition
    feedback = [hopeful_feedbacks[0]]
    if definition:
        feedback.append(definition)
    return ". ".join(feedback)


def generate_unknown_feedback():
    print("Within generate_unknown_feedback() function")

    return incorrect_feedbacks[0] + " " + "Please sound out the word and try again."


def generate_incorrect_feedback(rule_id, consec):
    rule = None if not rule_id else get_rule_by_id(rule_id)
    definition = None if not rule else rule.definition
    feedback = [incorrect_feedbacks[0]]
    if definition:
        feedback.append(definition)
    print("Within generate_incorrect_feedback() function",
          consec, "times", rule_id, rule, definition)
    return ". ".join(feedback)


def generate_hint_feedback(rule_id, consec):
    print("Within generate_hint_feedback() function")
    rule = None if not rule_id else get_rule_by_id(rule_id)
    hint = None if not rule else rule.hint
    if not hint:
        return generate_incorrect_feedback(rule_id, consec)
    feedback = [incorrect_feedbacks[0]]
    feedback.append(hint)
    return ". ".join(feedback)


def generate_answer_feedback(spelling_word, rule_id=None):
    print("Within generate_answer_feedback() function")
    rule = None if not rule_id else get_rule_by_id(rule_id)
    hint = None if not rule else rule.hint
    feedback = ["The correct spelling is '" + spelling_word + "'"]
    if hint:
        feedback.append("Remember to " + decapitalize_first_letter(hint))

    return ". ".join(feedback)
