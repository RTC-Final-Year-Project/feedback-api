from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Change_Y_To_I

rule = Rule_Change_Y_To_I

combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["happiness", "happiness"],
    ["buying", "buying"],
    ["crying", "crying"],
    ["trying", "trying"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["buying", "buiing"],
    ["crying", "criing"],
    ["trying", "triing"],
]

class Rule_Change_Y_To_I_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Change_Y_To_I_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule