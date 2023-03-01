import re
from .StandardRule import StandardRule

from ...utils import ldifference, bdifference

class Rule_Last_Consonant_Is_Doubled(StandardRule):
    """Test if a word follows the consonant doubling rule when adding certain suffixes."""
    id = 4
    definition = "The last consonant is doubled when adding the suffix 'ed', 'er', 'est', 'ing', 'y' when a short vowel sound precedes the consonant."
    
    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        # if consonant was not doubled, then attempted word is one char smaller  than actual word
        if len(actual_word) - 1 != len(attempted_word):
            return True
        [ldif_index, (actual_ldif_char, attempted_ldif_char)] = ldifference(actual_word, attempted_word)
        [bdif_index, (actual_bdif_char, attempted_bdif_char)] = bdifference(actual_word, attempted_word)
        
        actual_dif_chars = actual_word[ldif_index - 1: -bdif_index + 1]
        attempted_dif_chars = attempted_word[ldif_index - 1: -bdif_index + 1]

        # if actual dif is len 2 and attempted is len 1
        if len(attempted_dif_chars) == 1 and len(actual_dif_chars) == 2:
            # if actual is not a vowel
            if actual_dif_chars[0] not in ('a', 'e', 'i', 'o', 'u'):
                # if all chars match
                if actual_dif_chars[0] == actual_dif_chars[1] and actual_dif_chars[0] == attempted_dif_chars:
                    return False
        return True