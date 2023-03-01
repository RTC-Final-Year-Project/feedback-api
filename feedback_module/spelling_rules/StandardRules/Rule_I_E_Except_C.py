from .StandardRule import StandardRule

class Rule_I_E_Except_C(StandardRule):
  id = 10
  definition = "Use 'i' before 'e', except after 'c' and except when sounding like 'a'"
  examples = "niece, cashier, achieve; neighbour, weigh"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if ("cei" in actual_word
        and "cie" in attempted_word) or ("ie" in actual_word
                                         and "ei" in attempted_word):
      return False
    return True
  