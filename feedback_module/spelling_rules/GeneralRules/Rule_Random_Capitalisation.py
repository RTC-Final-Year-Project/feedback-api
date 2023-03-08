from .GeneralRule import GeneralRule

class Rule_Random_Capitalisation(GeneralRule):
  id = 27.5
  definition = "Words should not have random capitalisation of letters."
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    # length check - to ensure case matches even if number of letters in the words differ
    length=min(len(attempted_word), len(actual_word))
    for i in range(1, length):
      if (actual_word[i].isupper() and not attempted_word[i].isupper()) or (actual_word[i].islower() and not attempted_word[i].islower()):
        return False
    return True
  