import re
from .StandardRule import StandardRule

from ...utils import samedifference

class Rule_Change_Y_To_I_Except_Ing_Suffix(StandardRule):
    id = 13.6
    rule = "When a root ends in 'y', keep the 'y' if adding the suffix '-ing'"

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        if len(actual_word) != len(attempted_word):
            return True
        [dif_index, (actual_dif_char, attempted_dif_char)] = samedifference(actual_word, attempted_word)
        
        if dif_index != 0 and dif_index != len(actual_word):
            if actual_word.endswith("ing") and actual_dif_char == "y" and attempted_dif_char == "i":
                return False
        return True  
     


        
        
        
        
        
      