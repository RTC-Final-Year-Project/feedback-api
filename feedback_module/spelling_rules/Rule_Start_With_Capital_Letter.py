from .Rule import Rule

class Rule_Start_With_Capital_Letter(Rule):
  id = 27
  rule = "Proper nouns start with a capital letter"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if (actual_word[0].isupper() and not attempted_word[0].isupper()) or (actual_word[0].islower() and not attempted_word[0].islower()):
      return False
    return True