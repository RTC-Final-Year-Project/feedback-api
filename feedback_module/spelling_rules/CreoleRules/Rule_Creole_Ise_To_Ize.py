import re
from .CreoleRule import CreoleRule

class Rule_Creole_Ise_To_Ize(CreoleRule):
  id = 46
  definition = "Use of ise rather than ize"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if ((re.search("ise", actual_word, re.I)) and (re.search("ize", attempted_word, re.I) and not re.search("ise", attempted_word, re.I))):
      return False
    return True