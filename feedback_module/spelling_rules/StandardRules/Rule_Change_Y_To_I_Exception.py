import re
from .StandardRule import StandardRule

class Rule_Change_Y_To_I_Exception(StandardRule):
    id = 13.5
    rule = "The rule change a final y to i before a suffix, unless the suffix begins with i has exceptions, 'ier', 'ied','ies','iest'."

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        suffixes = ['ier', 'ied', 'ies', 'iest']
        for suffix in suffixes:
            if re.search(suffix + '$', actual_word) and not re.search('.?' + suffix + '$', attempted_word):
                return False
        return True


        
        
        
        
        
      