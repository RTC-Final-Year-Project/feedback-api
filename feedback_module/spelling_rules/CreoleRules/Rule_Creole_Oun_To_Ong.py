import re
from .CreoleRule import CreoleRule

class Rule_Creole_Oun_To_Ong(CreoleRule):
  id = 42
  definition = "This word has an 'oun' sound, not an 'ong' sound"
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    if ((re.search("oun", actual_word, re.I)) and (re.search("(ong|ung)", attempted_word, re.I) and not re.search("oun", attempted_word, re.I))):
      return False
    else:
      j=0
      while j <= len(actual_word):
        j = actual_word.find('oun', j)
        if j==-1:
          break
        if (attempted_word[j:j+3]=="ong" or attempted_word[j:j+3]=="ung"):
          return False
        j+=3
    return True