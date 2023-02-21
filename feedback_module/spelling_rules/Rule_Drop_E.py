###
import re
from .Rule import Rule

class Rule_Drop_E(Rule):
    id = 12
    rule = "Drop the final ‘e’ in a word before adding a suffix beginning with a vowel but not before a suffix beginning with a consonant."

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        """Test if the attempted word follows the rule: drop the final 'e' in a word before adding a suffix beginning with a vowel but not before a suffix beginning with a consonant."""

        # Check if the suffix begins with a vowel
        if attempted_word[0] in "aeiou":
            # Check if the word ends with 'e'
            if actual_word[-1] == "e":
                # Check if the suffix begins with a consonant
                if attempted_word[0] not in "aeiou":
                    return False
                else:
                    # Drop the final 'e' and add the suffix
                    return True
            else:
                # No need to drop the final 'e'
                return True
        else:
            # No need to drop the final 'e'
            return True
