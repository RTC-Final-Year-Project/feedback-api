import re
from .StandardRule import StandardRule

from ...utils import ldifference

class Rule_Ending_In_V_Or_J(StandardRule):
    id = 26
    rule = " Words don't usually end in 'v' or 'j', so there is likely a silent 'e' at the end"

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        # if 'e' was missing, then attempted word is one char smaller than actual word
        if (actual_word.endswith("je") and attempted_word.endswith("j")) or (not actual_word.endswith("dge") and actual_word.endswith("ge") and attempted_word.endswith("j")) or (actual_word.endswith("ve") and attempted_word.endswith("v")):
            return False
    
        return True