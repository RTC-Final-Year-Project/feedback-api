import re
from .StandardRule import StandardRule

from ...utils import ldifference

class Rule_Drop_E(StandardRule):
    id = 12
    rule = "Drop the final 'e' in a word before adding a suffix beginning with a vowel but not before a suffix beginning with a consonant."

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        """Test if the attempted word follows the rule: drop the final 'e' in a word before adding a suffix beginning with a vowel but not before a suffix beginning with a consonant."""
        # if 'e' was not dropped, then attempted word is one char larger than actual word
        if len(actual_word) + 1 != len(attempted_word):
            return True
        [dif_index, (actual_dif_char, attempted_dif_char)] = ldifference(actual_word, attempted_word)
        if attempted_dif_char == "e":
            suffixes = ['able', 'age', 'ed', 'est', 'ing', 'ion', 'ory', 'ous','er']
            for suffix in suffixes:
                if actual_word[dif_index:] == suffix and attempted_word[dif_index + 1:] == suffix:
                    return False
        return True
       
