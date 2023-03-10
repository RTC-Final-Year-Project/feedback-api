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


class SpellingAttemptData():
    def __init__(self):
        self.id = 0
        self.spelling_word = ""
        self.attempted_spelling = ""
        self.times_attempted = 0
        self.times_correct = 0
        self.rules_violated = []


action_history = {}
attempt_history = {}

max_actions_attempted = 7
max_consec_times_rule_violated = 3

def get_student_last_action(student_id):
    # TODO filter by attempt_id
    action_list = get_student_action_list(student_id)
    
    dict_len = len(action_list)
    
    if not dict_len:
        return None
    else:
        return action_list[dict_len - 1]

def get_student_action_list(student_id):
    action_list = action_history.get(student_id)
    if action_list == None:
        action_history[student_id] = []
        action_list = action_history[student_id]
    
    return action_list

def get_word_action_list(student_id, spelling_word):
    action_list = get_student_action_list(student_id)
    
    word_list = []
    for action in action_list:
        if action.spelling_word == spelling_word:
            word_list.append(action)
    
    return word_list

def get_student_last_word_action(student_id, spelling_word):
    # TODO filter by attempt_id
    action_list = get_word_action_list(student_id, spelling_word)
    
    dict_len = len(action_list)
    
    if not dict_len:
        return None
    else:
        return action_list[dict_len - 1]

def add_student_action(student_id, action_data: SpellingActionData):
    action_list = get_student_action_list(student_id)
    
    action_list.append(action_data)