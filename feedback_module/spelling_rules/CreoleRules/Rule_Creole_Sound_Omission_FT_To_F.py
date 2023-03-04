
from .CreoleRule import CreoleRule

class Rule_Creole_Sound_Omission_FT_To_F(CreoleRule):
  id = 35
  definition = "Final sound omission - ‘ft’ to ‘f’"
 
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if actual_word.endswith('ft') and attempted_word.endswith('f'):
        actual_prefix = actual_word[:-2]
        attempted_prefix = attempted_word[:-1]
        if actual_prefix == attempted_prefix:
            return False
    else:
        return True