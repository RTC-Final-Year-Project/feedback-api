from .spelling_history import get_word_action_list, get_student_last_word_action, SpellingActionData, max_actions_attempted, max_consec_times_rule_violated, add_student_action
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

def process_corrective_feedback(spelling_word, attempted_spelling, violated_rules, student_id, student_age = 10, student_action_history=[]):
    feedback = ""
    
    curr_word_action = SpellingActionData(spelling_word, attempted_spelling)

    if violated_rules == [None]:
        curr_word_action.spelled_correctly = True
    else:
        curr_word_action.num_violated_rules = len(violated_rules)
        violated_rules_ids = []
        for rule in violated_rules:
            violated_rules_ids.append(rule.get("id"))
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
        curr_word_action.max_violated_rules = max(last_word_action.max_violated_rules, curr_word_action.num_violated_rules)
        if not curr_word_action.spelled_correctly:
            if last_word_action.main_violated_rule_id in curr_word_action.violated_rules_ids:
                main_violated_rule_id = last_word_action.main_violated_rule_id
    
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
    if rule_violated_count == 1:
        pass # generate feedback with basic rule definition
    elif rule_violated_count == 2:
        pass # generate feedback with alternative definition if possible
    elif rule_violated_count == 3:
        pass # generate feedback with rule hint if available or alternative definition
    
    # if rule violated more than consec limit, just give answer should be true
    # stop processing after they get same rule wrong too many times in sequence
    if curr_word_action.consec_times_rule_violated > max_consec_times_rule_violated:
        feedback = generate_answer_feedback(spelling_word, curr_word_action.main_violated_rule_id)
        curr_word_action.just_give_answer = True
    
    
    # If multiple rules previously violated and less rules violated this time (started at like 3-4 but only 1 now): 	Give hopeful feedback.
    less_rule_violations_now = curr_word_action.num_violated_rules < last_word_action.num_violated_rules
    if less_rule_violations_now:
        feedback = generate_hopeful_feedback(spelling_word)
        
    # if word misspelled more than limit, just give answer should also be true
    # stop processing after they get same word wrong too many times in this attempt
    if curr_word_action.actions_attempted > max_actions_attempted:
        feedback = generate_answer_feedback(spelling_word)
        curr_word_action.just_give_answer = True
    
    # if last word was flagged as just give answer, be it the same here
    if last_word_action.just_give_answer:
        feedback = generate_answer_feedback(spelling_word)
        curr_word_action.just_give_answer = True
    
    if curr_word_action.spelled_correctly:
        # If word flagged as “just give answer” and correct spelling:
        # Give confirmation response. e.g. “That’s correct. No worries, you’re still learning!”
        if curr_word_action.just_give_answer:
            feedback = generate_confirmation_response(spelling_word)
        # elif
        # calculate_proficiency()
        
    # if previous action was not "just give answer", add to history
    if not last_word_action.just_give_answer:
        add_student_action(student_id, curr_word_action)

        

    # TODO If proficiency for this word is low, and got higher, upon correct spelling:
	# Give congratulatory response: e.g. “Excellent! You’re getting better at this word!”



def calculate_proficiency(student_id, spelling_word):
    pass

def generate_congratulatory_response():
    # e.g. “Excellent! You’re getting better at this word!”
    pass

def generate_confirmation_response():
    # e.g. “That’s correct. No worries, you’re still learning!”
    pass

def generate_hopeful_feedback():
    pass

def generate_answer_feedback(spelling_word, rule_id = None):
    hint = None if not rule_id else get_rule_by_id(rule_id)
    feedback = ["The correct spelling is '" + spelling_word + "'"]
    if hint:
        feedback.append("Remember to " + decapitalize_first_letter(hint))

    return ". ".join(feedback)

# def 
        