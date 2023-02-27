import re
from .StandardRule import StandardRule


class Rule_Ending_In_J(StandardRule):
    id = 26.5
    rule = "Words don't usually end in 'j', so there is likely a silent 'e' at the end"
    
    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        if (actual_word.endswith("je") and attempted_word.endswith("j")) or (not actual_word.endswith("dge") and actual_word.endswith("ge") and attempted_word.endswith("j")):
            return False
        return True
