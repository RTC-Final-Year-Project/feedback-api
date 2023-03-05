import re
from .StandardRule import StandardRule

from ...utils import samedifference

class Rule_Change_Y_To_I_Unless_Vowel_Before(StandardRule):
    id = 13.3
    definition = "When a root ends in 'y', keep the 'y' if a vowel comes before it"

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        if len(actual_word) != len(attempted_word):
            return True
        [dif_index, (actual_dif_char, attempted_dif_char)] = samedifference(actual_word, attempted_word)
        
        if dif_index != 0 and dif_index != len(actual_word):
            if not actual_word.endswith("ing") and actual_dif_char == "y" and attempted_dif_char == "i":
                return False
        
        return True  
     
        
