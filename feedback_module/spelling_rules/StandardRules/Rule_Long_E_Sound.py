from .StandardRule import StandardRule

class Rule_Long_E_Sound(StandardRule):
  id = 21
  definition = "When y is at the end of a 2 syllable word, it usually stands for the long e sound."
  examples='baby, penny, candy'
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if actual_word[-1] == 'y' and attempted_word[-2:] == 'ee':
        return False
    else:
        return True