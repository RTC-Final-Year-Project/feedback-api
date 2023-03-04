
from .CreoleRule import CreoleRule

class Rule_Creole_Sound_Omission_PT_To_P(CreoleRule):
  id = 37
  definition = "Final sound omission - ‘pt’ to ‘p’"
 
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if actual_word.endswith('pt') and attempted_word.endswith('p'):
        actual_prefix = actual_word[:-2]
        attempted_prefix = attempted_word[:-1]
        if actual_prefix == attempted_prefix:
            return False
    else:
        return True