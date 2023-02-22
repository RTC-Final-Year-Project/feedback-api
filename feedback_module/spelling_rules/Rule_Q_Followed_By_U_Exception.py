import re

from .Rule import Rule


class Rule_Q_Followed_By_U_Exception(Rule):
    id = 15.5
    rule = "The letter 'q' is usually followed by the letter 'u', but this word is an exception."
    examples = "Qatar, niqab"

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        if not (re.search("qu", actual_word, re.I)) and (re.search("qu", attempted_word, re.I)):
            return False
        return True
