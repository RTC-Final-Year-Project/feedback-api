import re
from .Rule import Rule

class Rule_Creole_Ending_In_I_N_G(Rule):
  id = 32
  rule = "Words ending with 'ing' should not be pronounced with an 'in' sound"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if (re.search("(in|n$)", attempted_word, re.I) and actual_word.endswith("ing")):
      return False
    return True