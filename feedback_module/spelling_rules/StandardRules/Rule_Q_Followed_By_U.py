import re

from .StandardRule import StandardRule

class Rule_Q_Followed_By_U(StandardRule):
  id = 15
  definition = "The letter 'q' is usually followed by the letter 'u'"
  examples = "queen, earthquake, quick"
  exceptions = "Qatar, niqab"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if re.search("qu", actual_word, re.I) and (re.search("q|u", attempted_word, re.I) and not re.search("qu", attempted_word, re.I)):
      return False
    return True
