from ..Rule import Rule

class GeneralRule(Rule):
  id = -2
  definition = ""
  examples = ""
  exception = ""
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    return True