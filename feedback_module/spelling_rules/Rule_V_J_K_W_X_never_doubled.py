import re
from .Rule import Rule

class Rule_S_Never_Follows_X(Rule):
  id = 17
  rule = "The consonants v, j, k, w and x are never doubled"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if "vv" in attempted_word or "jj" in attempted_word or "ww" in attempted_word or "kk" in attempted_word or "xx" in attempted_word:
      return False
    return True