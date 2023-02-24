###
import re
from .StandardRule import StandardRule

class Rule_Last_Consonant_Is_Doubled(StandardRule):
    """Test if a word follows the consonant doubling rule when adding certain suffixes."""
    id = 4
    rule = "The last consonant is doubled when adding the suffix 'ed’, ‘er’, ‘est’, ‘ing’, ‘y’ when a short vowel sound precedes the consonant."
    
    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        suffixes = ['ed', 'er', 'est', 'ing', 'y']
        for suffix in suffixes:
            if re.search(suffix + '$', actual_word) and not re.search(r'(.)(.)\2' + suffix + '$', attempted_word):
                return False
        return True
