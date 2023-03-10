class SpellingActionData():
    def __init__(self):
        self.spelling_word = ""
        self.attempted_spelling = ""
        self.spelled_correctly = False
        self.num_rules_violated = 0
        self.max_rules_violated = 0
        self.rules_violated = []
        self.main_rule_violated = 0
        self.just_give_answer = False
        self.emotion_given = ""
        self.definition_given = ""
        self.fuzzy_estimate = 0
        self.actions_attempted = 0
        self.consec_times_rule_violated = 0
    pass


class SpellingAttemptData():
    def __init__(self):
        self.spelling_word = ""
        self.attempted_spelling = ""
        self.times_attempted = 0
        self.times_correct = 0
        self.rules_violated = []
    pass


