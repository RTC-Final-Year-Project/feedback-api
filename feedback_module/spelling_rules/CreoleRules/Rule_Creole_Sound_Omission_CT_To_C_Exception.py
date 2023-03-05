
from .CreoleRule import CreoleRule

class Rule_Creole_Sound_Omission_CT_To_C_Exception(CreoleRule):
  id = 34.5
  definition = "Final sound omission are usually ‘ct’ to ‘c’ however 'ck' is an exception"
 
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if actual_word.endswith('ct') and attempted_word.endswith('ck'):
        actual_prefix = actual_word[:-2]
        attempted_prefix = attempted_word[:-2]
        if actual_prefix == attempted_prefix:
            return False
    else:
        return True