import re

from .StandardRule import StandardRule

class Rule_Q_Followed_By_U(StandardRule):
  id = 15
  definition = "The letter 'q' is usually followed by the letter 'u'"
  examples = "queen, earthquake, quick"
  exceptions = "Qatar, niqab"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if re.search("qu", actual_word, re.I) and (re.search("q", attempted_word, re.I) and not re.search("qu", attempted_word, re.I)):
      # extra logic needed for cases where the q is randomly placed eg: quick --> kwiq - should not violate this rule
      j = actual_word.find('qu')
      if (j+1) <= len(attempted_word)-1:
        if (attempted_word[j]=='q') and not (attempted_word[j+1]=='u'):
          return False
    return True
  