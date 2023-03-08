import re
from .CreoleRule import CreoleRule

class Rule_Creole_Wh_To_W(CreoleRule):
  id = 40
  definition = "'Wh' is not pronounced with a hard 'w' sound"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if ((re.search("wh", actual_word, re.I)) and (re.search("w", attempted_word, re.I) and not re.search("wh", attempted_word, re.I))):
      j = actual_word.find('wh')
      i = attempted_word.find('w')
      if (j>i):
        return True
      return False
    return True