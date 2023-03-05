
from .CreoleRule import CreoleRule

class Rule_Creole_Sound_Omission_LD_To_L_Exception(CreoleRule):
  id = 38.5
  definition = "Final sound omission usually  ‘ld’ to ‘l’ however 'le' is an exception"
 
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if actual_word.endswith('ld') and attempted_word.endswith('le'):
        actual_prefix = actual_word[:-2]
        attempted_prefix = attempted_word[:-2]
        if actual_prefix == attempted_prefix:
            return False
    else:
        return True