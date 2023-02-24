import re
from .StandardRule import StandardRule

class Rule_Ending_In_V_Or_J(StandardRule):
  id = 26
  rule = " Words don't usually end in 'v' or 'j', so there is likely a silent 'e' at the end"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if (re.search("(v|j)$", attempted_word, re.I) and (actual_word.endswith("e"))):
      return False
    return True