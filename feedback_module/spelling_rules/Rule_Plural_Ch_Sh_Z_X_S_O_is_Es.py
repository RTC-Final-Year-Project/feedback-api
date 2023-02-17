import re

from .Rule import Rule

class Rule_Plural_Ch_Sh_Z_X_S_O_is_Es(Rule):
  id = 6
  rule = "To form the plural for nouns ending in ‘ch’, ‘sh’, ‘z’, ‘x’, ‘s’, ‘o’, you add ‘es’"
  examples = "churches, watches, foxes, echoes"
  exceptions = "radios, solos, pianos, photos"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    actual_has_es = re.search("(ch|sh|z|x|s|o)es$", actual_word)
    attempts_end_matches = False
  
    if actual_has_es:
      attempts_end_matches = re.search(actual_has_es.group() + "$",
                                       attempted_word)
  
    if attempts_end_matches == None:
      return False
  
    return True