
from .CreoleRule import CreoleRule

class Rule_Creole_Sound_Omission_SK_To_S(CreoleRule):
  id = 39
  definition = "Final sound omission - ‘sk’ to ‘s’"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if actual_word.endswith('sk') and attempted_word.endswith('s'):
        actual_prefix = actual_word[:-2]
        attempted_prefix = attempted_word[:-1]
        if actual_prefix == attempted_prefix:
            return False
    else:
        return True