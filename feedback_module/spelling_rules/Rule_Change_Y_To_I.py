###
import re
from .Rule import Rule

class Rule_Change_Y_To_I(Rule):
    id = 13
    rule = "Change a final y to i before a suffix, unless the suffix begins with i."

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        suffixes_with_i = ["ing", "ish", "ism", 'ist', 'ize', 'ive', 'ify']  # list of suffixes that begin with i
        # if actual_word[-1] == "y" and attempted_word[-1] != "y":
            # actual_word ends with y but attempted_word doesn't
        if attempted_word[-3:] not in suffixes_with_i:
                # the last three characters of the attempted word are not a suffix beginning with i
            return False
            # the last three characters of attempted_word are a suffix beginning with i
        if attempted_word[-3:] in suffixes_with_i and attempted_word[-3:] != 'y':
            return True

