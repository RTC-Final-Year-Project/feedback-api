###
import re
from .PluralRule import PluralRule

class Rule_Plural_By_Adding_S(PluralRule):
    id = 7
    rule = "For most nouns the plural is formed by adding ‘s’"

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        if actual_word.endswith('s') and attempted_word.endswith('s'):
            return actual_word[:-1] == attempted_word[:-1]
        return False
        


