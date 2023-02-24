import re

from .StandardRule import StandardRule

class Rule_Ending_In_E_Y(StandardRule):
  id = 24
  rule = "When the letters 'ey' are at the end of a 2 syllable word, they usually stand for the long e sound."
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if (re.search("ey$", actual_word, re.I) and not re.search("ey", attempted_word, re.I) and re.search("(ie|e|i|y)$", attempted_word, re.I)  ):
      return False
    return True
