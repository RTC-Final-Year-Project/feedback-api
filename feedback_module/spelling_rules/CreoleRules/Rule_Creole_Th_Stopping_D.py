import re
from .CreoleRule import CreoleRule

class Rule_Creole_Th_Stopping_D(CreoleRule):
  id = 29
  definition = "'Th' is not pronounced with a hard 'd' sound"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if ((re.search("(d)", attempted_word, re.I) and not re.search("th", attempted_word, re.I)) and re.search("th", actual_word, re.I)):
      return False
    return True