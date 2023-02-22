from .AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_S_Never_Follows_X


rule = Rule_S_Never_Follows_X

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["excite", "excite"],
    ["Max", "max"],
    ["lives", "lives"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["excite", "exsite"],
    ["excess", "exsess"],
    ["max", "maxs"],
]

class Rule_S_Never_Follows_X_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_S_Never_Follows_X_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule