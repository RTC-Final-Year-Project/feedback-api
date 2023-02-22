import re
from .Rule import Rule

class Rule_Creole_Th_Stopping_T(Rule):
  id = 29
  rule = "'Th' is not pronounced with a hard 'd' or hard 't' sound"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if ((re.search("(t)", attempted_word, re.I) and not re.search("th", attempted_word, re.I)) and re.search("th", actual_word, re.I)):
      return False
    return True