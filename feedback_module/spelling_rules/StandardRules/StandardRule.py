from ..Rule import Rule

class StandardRule(Rule):
  id = -3
  rule = ""
  examples = ""
  exception = ""
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    return True