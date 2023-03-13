import re
from .CreoleRule import CreoleRule

class Rule_Creole_Our_To_Or(CreoleRule):
  id = 45
  definition = "Use of or rather than our"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if ((re.search("our", actual_word, re.I)) and (re.search("or", attempted_word, re.I) and not re.search("our", attempted_word, re.I))):
      return False
    return True