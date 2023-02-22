import re
from .Rule import Rule

class Rule_Change_Y_To_I(Rule):
    id = 13
    rule = "Change a final y to i before a suffix, unless the suffix begins with i."

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        suffixes = ["ing", "ish", "ism", 'ist', 'ize', 'ive', 'ify']
        for suffix in suffixes:
            if re.search(suffix + '$', actual_word) and not re.search('y' + suffix + '$', attempted_word):
                return False
        return True
        
        
     
        
        
      