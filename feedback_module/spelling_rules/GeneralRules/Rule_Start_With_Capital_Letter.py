from .GeneralRule import GeneralRule

class Rule_Start_With_Capital_Letter(GeneralRule):
  id = 27
  # definition = "Proper nouns start with a capital letter"
  definition = "This word is not a proper noun and should not start with a capital letter."
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if (actual_word[0].isupper() and not attempted_word[0].isupper()) or (actual_word[0].islower() and not attempted_word[0].islower()):
      return False
    return True
  
# TODO:
# May need to alter to account for if the student includes some random capital letter OR use a separate rule
# eg: actual_word = "queen"; attempted_word="quEen"
  