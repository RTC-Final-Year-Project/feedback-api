
from .CreoleRule import CreoleRule

class Rule_Creole_Sound_Omission_ID_To_I(CreoleRule):
  id = 34
  definition = "Final sound omission - ‘id’ to ‘i’"
 
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if actual_word.endswith('id') and attempted_word.endswith('i'):
        actual_prefix = actual_word[:-2]
        attempted_prefix = attempted_word[:-1]
        if actual_prefix == attempted_prefix:
            return False
    else:
        return True