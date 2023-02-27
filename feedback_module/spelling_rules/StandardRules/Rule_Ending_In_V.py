import re
from .StandardRule import StandardRule

class Rule_Ending_In_V(StandardRule):
  id = 26.5
  rule = " Words don't usually end in 'v', so there is likely a silent 'e' at the end"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if (re.search("v$", attempted_word, re.I) and (re.search("e$", actual_word, re.I))):
      return False
    return True