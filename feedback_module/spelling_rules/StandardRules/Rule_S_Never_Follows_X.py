from .StandardRule import StandardRule

class Rule_S_Never_Follows_X(StandardRule):
  id = 16
  rule = "The letter s never follows x"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if "xs" in attempted_word:
      return False
    return True