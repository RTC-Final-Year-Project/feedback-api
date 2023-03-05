from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Last_Consonant_Is_Doubled

rule = Rule_Last_Consonant_Is_Doubled

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["planner", "planner"],
    ["beginning", "beginning"],
    ["stopped", "stopped"],
    ["Fattest", "Fattest"],
    ["happy", "happy"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["planner", "planer"],
    ["beginning", "begining"],
    ["stopped", "stoped"],
    ["fattest", "fatest"],
    ["happy", "hapy"],
]


class Rule_Last_Consonant_Is_Doubled_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Last_Consonant_Is_Doubled_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule