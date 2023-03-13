
from .CreoleRule import CreoleRule

class Rule_Creole_Word_Shortening(CreoleRule):
  id = 43
  definition = "word shortening"
  examples = 'trickry instead of trickery'
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    actual_suffix = actual_word[-3:]
    attempted_suffix = attempted_word[-3:]
    
    if actual_suffix != attempted_suffix:
        if not any(vowel in actual_suffix for vowel in "aeiou"):
            return False
    return True