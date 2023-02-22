###
import re
from .Rule import Rule

class Rule_Drop_E(Rule):
    id = 12
    rule = "Drop the final ‘e’ in a word before adding a suffix beginning with a vowel but not before a suffix beginning with a consonant."

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        """Test if the attempted word follows the rule: drop the final 'e' in a word before adding a suffix beginning with a vowel but not before a suffix beginning with a consonant."""
        suffixes = ['able', 'age', 'ed', 'est', 'ing', 'ion', 'ory', 'ous','er']
        for suffix in suffixes:
            if re.search(suffix + '$', actual_word) and not re.search('[^e]'+ suffix + '$', attempted_word):
                return False
        return True
       
