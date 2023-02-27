import re
from .CreoleRule import CreoleRule

class Rule_Creole_Th_Stopping_T(CreoleRule):
  id = 30
  rule = "'Th' is not pronounced with a hard 't' sound"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if ((re.search("t", attempted_word, re.I) and not re.search("th", attempted_word, re.I)) and re.search("th", actual_word, re.I)):
      return False
    return True