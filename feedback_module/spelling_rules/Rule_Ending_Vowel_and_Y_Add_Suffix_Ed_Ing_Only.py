import re

from .Rule import Rule

class Rule_Ending_Vowel_and_Y_Add_Suffix_Ed_Ing_Only(Rule):
  id = 23
  rule = "Words ending in a vowel and y can add the suffix -ed or -ing without making any other change."
  examples="buying, delaying, employed"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    actual_has_es = re.search("[AEIOU]y(ed|ing)$", actual_word, re.I)
    attempts_end_matches = False


  
    if actual_has_es:
      attempts_end_matches = re.search(actual_has_es.group() + "$",
                                       attempted_word, re.I)
  
    if attempts_end_matches == None:
      return False
  
    return True