from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Long_Vowel


rule = Rule_Long_Vowel

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [ 
    ["boat", "boat"],
    ["cheap", "cheap"],
    ["paid", "paid"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["boat", "boot"],
    ["cheap", "cheep"],
    ["paid", "paad"],
]

class Rule_Long_Vowel_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Long_Vowel_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule