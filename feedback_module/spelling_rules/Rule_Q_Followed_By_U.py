import re

from .Rule import Rule

class Rule_Q_Followed_By_U(Rule):
  id = 15
  rule = "The letter ‘q’ is usually followed by the letter ‘u’"
  examples = "queen, earthquake, quick"
  exceptions = "Qatar, niqab"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if re.search("qu", actual_word, re.I) and not re.search("qu", attempted_word, re.I):
      return False
    return True
