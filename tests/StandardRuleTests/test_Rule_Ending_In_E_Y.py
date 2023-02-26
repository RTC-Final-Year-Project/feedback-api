from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Ending_In_E_Y


rule = Rule_Ending_In_E_Y

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["donkey", "dongkey"],
    ["money", "money"],
    ["fairy", "fairey"],
    ["funny", "funny"],
    ["prairie", "prairie"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["donkey", "donkie"],
    ["donkey", "donke"],
    ["donkey", "donki"],
    ["donkey", "donkii"],
    ["donkey", "donky"],
]

class Rule_Ending_In_E_Y_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Ending_In_E_Y_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule