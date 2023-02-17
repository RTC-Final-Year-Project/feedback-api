import re
from .Rule import Rule

class Rule_Ending_In_D_G_E(Rule):
  id = 26
  rule = "Some words use 'dge' when there’s a ‘j’ sound"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if (re.search("(g|ge|dg|j)$", attempted_word, re.I) and actual_word.endswith("dge")):
      return False
    return True