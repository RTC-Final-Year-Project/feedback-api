###
import re
from .Rule import Rule

class Rule_Plural_by_Adding_S(Rule):
    id = 7
    rule = "For most nouns the plural is formed by adding ‘s’"

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        # Check if the word is plural (i.e., ends with 's' or 'es')
        if word.endswith(("s", "es")):
            # Check if the singular form is the same as the plural form without the last letter
            if word[:-1] == word[:-2] or word[:-1] == word[:-3]:
                return True
            else:
                return False
        else:
            return False