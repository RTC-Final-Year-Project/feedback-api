from .StandardRule import StandardRule

class Rule_Long_Vowel(StandardRule):
  id = 20
  definition = "To make a long vowel sound, you need to add a second vowel."
  examples='boat, cheap, paid'
  
  @staticmethod
  def check_if_followed(actual_word, attempted_word):
    # Define a set of vowels
    vowels = set('aeiou')
    # Find the first vowel in the attempted_word
    first_vowel_index = -1
    for i in range(len(attempted_word)):
        if attempted_word[i] in vowels:
            first_vowel_index = i
            break
    # If there is no vowel in the attempted_word or the first vowel is the last letter
    if first_vowel_index == -1 or first_vowel_index == len(attempted_word) - 1:
        return False
    # Check if the letter after the first vowel is different
    return attempted_word[first_vowel_index+1] != attempted_word[first_vowel_index]
