from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Wh_To_W

rule = Rule_Creole_Wh_To_W

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["whine", "whine"],
    ["where", "where"],
    ["with", "width"],
    ["what", "what"],
    ["water", "whater"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["whine", "wine"],
    ["where", "wear"],
    ["whale", "wale"],
    ["where", "wey"],
    ["what", "wot"],
    ["what", "wat"],
]

class Rule_Creole_Wh_To_W_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Wh_To_W_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule