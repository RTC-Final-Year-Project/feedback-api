
from .CreoleRule import CreoleRule

class Rule_Creole_Sound_Omission_CT_To_C(CreoleRule):
  id = 34
  definition = "Final sound omission - ‘ct’ to ‘c’"
 
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if actual_word.endswith('ct') and attempted_word.endswith('c'):
        actual_prefix = actual_word[:-2]
        attempted_prefix = attempted_word[:-1]
        if actual_prefix == attempted_prefix:
            return False
    else:
        return True