import re

from .StandardRule import StandardRule

class Rule_K(StandardRule):
  id = 9
  rule = "The letter 'k' is used on its own when the short vowel sound is followed by a consonant or when preceded by a long vowel sound"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if (re.search("k", actual_word, re.I) and not re.search("ck", actual_word, re.I) and re.search("ck", attempted_word, re.I)):
      return False
    return True
