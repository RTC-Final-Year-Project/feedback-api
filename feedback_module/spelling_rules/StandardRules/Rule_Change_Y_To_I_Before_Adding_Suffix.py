import re
from .StandardRule import StandardRule

from ...utils import samedifference

class Rule_Change_Y_To_I_Before_Adding_Suffix(StandardRule):
    id = 13
    rule = "When a root ends in 'y', change the 'y' to 'i' before adding the suffix"

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        if len(actual_word) != len(attempted_word):
            return True
        [dif_index, (actual_dif_char, attempted_dif_char)] = samedifference(actual_word, attempted_word)
        
        if dif_index != 0 and dif_index != len(actual_word):
            if actual_dif_char == "i" and attempted_dif_char == "y":
                return False
        
        return True  
     
        
