###
import re
from .Rule import Rule

class Rule_Last_Consonant_is_doubled(Rule):
    """Test if a word follows the consonant doubling rule when adding certain suffixes."""
    id = 4
    rule = "The last consonant is doubled when adding the suffix ‘ed’, ‘er’, ‘est’, ‘ing’, ‘y’ when a short vowel sound precedes the consonant."
    
    @staticmethod
    # Assuming that attempted_word is a lowercase string with no punctuation or whitespace.
    def check_if_followed(actual_word, attempted_word):
        # Define the regular expression pattern to match a short vowel sound followed by a consonant
        pattern = re.compile(r"[aeiou][^aeiouwyx]{1}[a-z]*$")

        # Check if the word matches the pattern
        if pattern.search(attempted_word):
            # Check if the last letter is a consonant that can be doubled
            if attempted_word[-1] in "bcdgjklmnpqrstvwxyz":
                # Check if the word ends with one of the eligible suffixes
                if attempted_word.endswith(("ed", "er", "est", "ing", "y")):
                    # Check if the last consonant is already doubled
                    if attempted_word[-2] == attempted_word[-1]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
