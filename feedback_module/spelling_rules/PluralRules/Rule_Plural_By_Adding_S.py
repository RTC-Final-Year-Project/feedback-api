###
import re
from .PluralRule import PluralRule

class Rule_Plural_By_Adding_S(PluralRule):
    id = 7
    definition = "For most nouns the plural is formed by adding 's'"

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        if not actual_word.endswith("es") and actual_word.endswith("s"):
            len_before = len(actual_word[:-1])
            if actual_word[:len_before] == attempted_word[:len_before]:
                if actual_word[len_before:] != attempted_word[len_before:]:
                    return False
        return True
        


