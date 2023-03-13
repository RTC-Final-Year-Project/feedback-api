# import re
# from .CreoleRule import CreoleRule

# class Rule_Creole_Ture_To_Tya(CreoleRule):
#   id = 49
#   definition = "Use of tya rather than ture"
  
#   @staticmethod
#   def check_if_followed(actual_word, attempted_word):
#     if ((re.search("ture", actual_word, re.I)) and (re.search("tya", attempted_word, re.I) and not re.search("ture", attempted_word, re.I))):
#       return False
#     return True