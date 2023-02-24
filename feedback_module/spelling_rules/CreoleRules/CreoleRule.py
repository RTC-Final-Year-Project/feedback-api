from ..Rule import Rule

class CreoleRule(Rule):
  id = -5
  rule = ""
  examples = ""
  exception = ""
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    return True