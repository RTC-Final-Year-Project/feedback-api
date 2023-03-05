from .StandardRule import StandardRule

class Rule_CE_Sound_Like_S(StandardRule):
  id = 28
  definition = "‘ce’ sometimes makes an ‘s’ sound"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    # Find the index of 'ce' in the actual_word
    ce_index = actual_word.find('ce')
    # If 'ce' is not found in the actual_word, return True
    if ce_index == -1:
        return True
    # Check if there is an 's' at the same index in the attempted_word
    if attempted_word[ce_index] == 's':
        return False
    else:
        return True