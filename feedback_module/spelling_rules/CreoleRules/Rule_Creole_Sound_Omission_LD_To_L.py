
from .CreoleRule import CreoleRule

class Rule_Creole_Sound_Omission_LD_To_L(CreoleRule):
  id = 38
  definition = "Final sound omission - âldâ to âlâ"
 
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if actual_word.endswith('ld') and attempted_word.endswith('l'):
        actual_prefix = actual_word[:-2]
        attempted_prefix = attempted_word[:-1]
        if actual_prefix == attempted_prefix:
            return False
    else:
        return True