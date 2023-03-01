from ..Rule import Rule

class CreoleRule(Rule):
  id = -5
  definition = ""
  examples = ""
  exception = ""
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    return True