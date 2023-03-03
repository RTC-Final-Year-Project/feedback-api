from .PluralRule import PluralRule

class Rule_Plural_By_Change_Y_To_I_Add_Es(PluralRule):
    id = 19
    definition = "To make a word plural, if the word ends with a consonant and y, change the y to an i and add es."
    examples='babies'

    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        if not attempted_word.endswith('ies') and actual_word[-4] not in ['a', 'e', 'i', 'o', 'u'] and actual_word.endswith('ies'):
            return  False
        return True
       