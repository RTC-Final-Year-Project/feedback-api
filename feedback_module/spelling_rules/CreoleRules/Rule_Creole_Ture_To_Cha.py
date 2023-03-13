import re
from .CreoleRule import CreoleRule

class Rule_Creole_Ture_To_Cha(CreoleRule):
  id = 47
  definition = "Use of cha rather than ise"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if ((re.search("ture", actual_word, re.I)) and (re.search("cha", attempted_word, re.I) and not re.search("ture", attempted_word, re.I))):
      return False
    return True