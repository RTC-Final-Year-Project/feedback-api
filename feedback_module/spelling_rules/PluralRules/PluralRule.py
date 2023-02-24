from ..Rule import Rule

class PluralRule(Rule):
  id = -4
  rule = ""
  examples = ""
  exception = ""
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    return True