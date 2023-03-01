import re
from .CreoleRule import CreoleRule

class Rule_Creole_Th_Stopping_T(CreoleRule):
  id = 30
  definition = "'Th' is not pronounced with a hard 't' sound"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if ((re.search("th", actual_word, re.I)) and (re.search("t", attempted_word, re.I) and not re.search("th", attempted_word, re.I))):
      j = actual_word.find('th')
      i = attempted_word.find('t')
      # extra logic needed for cases where there are multiple t's like photosynthesis - photosynsis --> shouldnt violate this rule
      if (j>i):
        return True
      return False
    return True