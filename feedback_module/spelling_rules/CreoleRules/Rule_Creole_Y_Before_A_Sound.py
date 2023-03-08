import re
from .CreoleRule import CreoleRule

class Rule_Creole_Y_Before_A_Sound(CreoleRule):
  id = 31
  definition = "A 'y' sound is not present before the 'a' sound"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if (re.search("ya", attempted_word, re.I)) and not (re.search("ya", actual_word, re.I)):
      j = actual_word.find('a')
      i = attempted_word.find('y')
      if (i+3==j):
        return True
      return False
    return True