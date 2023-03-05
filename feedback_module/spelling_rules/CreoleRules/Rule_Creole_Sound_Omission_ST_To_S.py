
from .CreoleRule import CreoleRule

class Rule_Creole_Sound_Omission_ST_To_S(CreoleRule):
  id = 33
  definition = "Final sound omission (Consonant cluster reduction) - ‘st’ to ‘s'"
  examples='just, first, best, dust'
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if actual_word.endswith('st') and attempted_word.endswith('s'):
        actual_prefix = actual_word[:-2]
        attempted_prefix = attempted_word[:-1]
        if actual_prefix == attempted_prefix:
            return False
    else:
        return True