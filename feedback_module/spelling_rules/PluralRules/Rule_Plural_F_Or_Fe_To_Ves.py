from .PluralRule import PluralRule

class Rule_Plural_F_Or_Fe_To_Ves(PluralRule):
    id = 5
    rule = "To form the plural for nouns ending in 'f' or 'fe', change the 'f' or 'fe' to 'v' and then add 'es'"
    examples = "life/lives, knife/knives, wolf/wolves"
    
    @staticmethod
    def check_if_followed(actual_word, attempted_word):
        if actual_word.endswith("ves") and (attempted_word.endswith("fes")
                                            or attempted_word.endswith("fs")
                                            or attempted_word.endswith("vs")):
            return False
        return True