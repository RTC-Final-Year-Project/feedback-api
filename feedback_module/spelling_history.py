from typing import Dict, List


class SpellingActionData():
    def __init__(self, spelling_word, attempted_spelling):
        self.attempt_id = ""
        self.spelling_word = spelling_word
        self.attempted_spelling = attempted_spelling
        self.spelled_correctly = False
        self.num_violated_rules = 0
        self.max_violated_rules = 0
        self.violated_rules_ids = []
        self.main_violated_rule_id = 0
        self.just_give_answer = False
        self.emotion_given = ""
        self.definition_given = ""
        self.fuzzy_estimate = 0
        self.actions_attempted = 0
        self.consec_times_rule_violated = 0
        self.recorded_attempt = False

    def __repr__(self):
        return str(dict(
            attempt_id=self.attempt_id,
            spelling_word=self.spelling_word,
            attempted_spelling=self.attempted_spelling,
            spelled_correctly=self.spelled_correctly,
            num_violated_rules=self.num_violated_rules,
            max_violated_rules=self.max_violated_rules,
            violated_rules_ids=self.violated_rules_ids,
            main_violated_rule_id=self.main_violated_rule_id,
            just_give_answer=self.just_give_answer,
            emotion_given=self.emotion_given,
            definition_given=self.definition_given,
            fuzzy_estimate=self.fuzzy_estimate,
            actions_attempted=self.actions_attempted,
            consec_times_rule_violated=self.consec_times_rule_violated,
            recorded_attempt=self.recorded_attempt,
        ))


class SpellingAttemptData():
    def __init__(self, id, spelling_word, actions_attempted, spelled_correctly):
        self.id = id
        self.spelling_word = spelling_word
        self.actions_attempted = min(actions_attempted, max_actions_attempted)
        self.spelled_correctly = spelled_correctly
        self.rules_violated = []
        self.attempt_score = 0

        self.calculate_score()

    def calculate_score(self):
        attempt = self.actions_attempted
        max_attempts = max_actions_attempted
        score = 1 - pow(((attempt - 1) / max_attempts), __ALPHA__)
        self.attempt_score = score
        print("Calculated score:", score)


__ALPHA__ = 0.65
action_history: Dict[str, List[SpellingActionData]] = {}
attempt_history: Dict[str, List[SpellingAttemptData]] = {}

student_word_proficiencies: Dict[str, Dict[str, int]] = {}

max_actions_attempted = 7
max_consec_times_rule_violated = 3


def get_student_last_action(student_id) -> SpellingActionData:
    # TODO filter by attempt_id
    action_list = get_student_action_list(student_id)

    dict_len = len(action_list)

    if not dict_len:
        return None
    else:
        return action_list[dict_len - 1]


def get_student_action_list(student_id) -> List[SpellingActionData]:
    action_list = action_history.get(student_id)
    if action_list == None:
        action_history[student_id] = []
        action_list = action_history[student_id]

    return action_list


def get_word_action_list(student_id, spelling_word) -> List[SpellingActionData]:
    action_list = get_student_action_list(student_id)

    word_list = []
    for action in action_list:
        if action.spelling_word == spelling_word:
            word_list.append(action)

    return word_list


def get_student_last_word_action(student_id, spelling_word) -> SpellingActionData:
    # TODO filter by attempt_id
    action_list = get_word_action_list(student_id, spelling_word)

    dict_len = len(action_list)

    if not dict_len:
        return None
    else:
        return action_list[dict_len - 1]


def add_student_action(student_id, action_data: SpellingActionData):
    print("Added student action")
    action_list = get_student_action_list(student_id)

    action_list.append(action_data)


def get_student_attempt_list(student_id) -> List[SpellingAttemptData]:
    attempt_list = attempt_history.get(student_id)
    if attempt_list == None:
        attempt_history[student_id] = []
        attempt_list = attempt_history[student_id]

    return attempt_list


def add_student_attempt(session_id, student_id: str, attempt_data: SpellingAttemptData):
    attempt_list = get_student_attempt_list(student_id)
    for attempt in attempt_list:
        if attempt.id == session_id:
            return False
    attempt_list.append(attempt_data)
    return True


def update_word_proficiency(student_id: str, word: str, score: int) -> int:
    proficiency = score
    curr_word_proficiency = get_word_proficiency(student_id, word)
    if curr_word_proficiency == -1:  # this means it is attempt 1
        proficiency = score
    else:
        proficiency = ((1 - __ALPHA__) * curr_word_proficiency) + \
            (__ALPHA__ * score)

    set_student_word_proficiency(student_id, word, proficiency)
    
    print("Updated proficiency:", score, curr_word_proficiency, proficiency)

    return proficiency


def set_student_word_proficiency(student_id, word, proficiency):
    student_proficiency = get_student_proficiency(student_id)
    student_proficiency[word] = proficiency


def get_word_proficiency(student_id: str, word: str) -> int:
    student_proficiency = get_student_proficiency(student_id)
    word_proficiency = student_proficiency.get(word)
    if word_proficiency == None:
        student_proficiency[word] = -1
        word_proficiency = student_proficiency[word]

    return word_proficiency


def get_student_proficiency(student_id: str) -> Dict[str, int]:
    student_proficiency_dict = student_word_proficiencies.get(student_id)
    if student_proficiency_dict == None:
        student_word_proficiencies[student_id] = {}
        student_proficiency_dict = student_word_proficiencies[student_id]

    return student_proficiency_dict
