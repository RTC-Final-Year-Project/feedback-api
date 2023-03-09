import re
from .CreoleRule import CreoleRule

class Rule_Creole_Omitted_R_Sound(CreoleRule):
  id = 44
  definition = "Pay attention to the ending 'r' sound in the word"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    combo_set = ["ar", "er", "or"]
    for item in combo_set:
      if (re.search(item, actual_word, re.I) and not re.search(item, attempted_word, re.I)):
        return False
    return True