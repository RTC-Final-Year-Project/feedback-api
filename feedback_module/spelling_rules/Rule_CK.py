import re

from .Rule import Rule

class Rule_CK(Rule):
  id = 8
  rule = "'ck' is used following a short vowel sound"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if re.search("ck", actual_word, re.I) and not re.search("ck", attempted_word, re.I):
      return False
    return True
