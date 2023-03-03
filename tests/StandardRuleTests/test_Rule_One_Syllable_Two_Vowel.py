from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_One_Syllable_Two_Vowel


rule = Rule_One_Syllable_Two_Vowel

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["wheel", "wheel"],
    ["wheel", "weel"],
    ["team", "team"],
    ["queen", "queen"],
    ["leaf", "leaf"],
    
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["leaf", "lef"],
    ["team", "tem"],
    ["light", "ligh"],
]

class Rule_One_Syllable_Two_Vowel_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_One_Syllable_Two_Vowel_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule