from .AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_I_E_Except_C


rule = Rule_I_E_Except_C

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["receive", "receive"],
    ["retrieve", "retrieve"],
    ["lives", "lives"],
    ["reception", "receive"],
    ["chief", "chief"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["receive", "recieve"],
    ["conceive", "concieve"],
    ["retrieve", "retreive"],
    ["chief", "cheif"],
]

class Rule_I_E_Except_C_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_I_E_Except_C_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule