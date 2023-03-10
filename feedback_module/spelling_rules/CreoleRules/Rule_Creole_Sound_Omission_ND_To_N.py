
from .CreoleRule import CreoleRule

class Rule_Creole_Sound_Omission_ND_To_N(CreoleRule):
  id = 36
  definition = "Final sound omission - βndβ to βdβ"
 
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if actual_word.endswith('nd') and attempted_word.endswith('n'):
        actual_prefix = actual_word[:-2]
        attempted_prefix = attempted_word[:-1]
        if actual_prefix == attempted_prefix:
            return False
    else:
        return True