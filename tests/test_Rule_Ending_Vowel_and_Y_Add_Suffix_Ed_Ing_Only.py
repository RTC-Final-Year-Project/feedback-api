from .AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Ending_Vowel_and_Y_Add_Suffix_Ed_Ing_Only


rule = Rule_Ending_Vowel_and_Y_Add_Suffix_Ed_Ing_Only

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["happy", "happy"],
    ["buying", "buying"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["buying", "buyin"],
    ["employed", "emploid"],
    ["delaying", "delayin"],
]

class Rule_Ending_Vowel_and_Y_Add_Suffix_Ed_Ing_Only_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Ending_Vowel_and_Y_Add_Suffix_Ed_Ing_Only_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule