from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Ending_In_V_Or_J


rule = Rule_Ending_In_V_Or_J

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["edge", "edge"],
    ["judge", "judge"],
    ["rummage", "rummage"],
    ["hive", "hive"],
    ["live", "live"],
    ["positive", "positive"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["hive", "hyv"],
    ["judge", "juj"],
    ["hedge", "hej"],
    ["live", "liv"],
    ["rummage", "rumej"],
    ["positive", "positiv"],
]

class Rule_Ending_In_V_Or_J_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Ending_In_V_Or_J_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule