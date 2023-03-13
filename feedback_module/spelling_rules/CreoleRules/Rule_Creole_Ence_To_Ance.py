import re
from .CreoleRule import CreoleRule

class Rule_Creole_Ence_To_Ance(CreoleRule):
  id = 48
  definition = "Use of ance rather than ence"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if ((re.search("ence", actual_word, re.I)) and (re.search("ance", attempted_word, re.I) and not re.search("ence", attempted_word, re.I))):
      return False
    return True