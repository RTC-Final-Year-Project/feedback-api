from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Ending_In_Ing

rule = Rule_Creole_Ending_In_Ing

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["asking", "asking"],
    ["falling", "falling"],
    ["telling", "telling"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["asking", "askin"],
    ["falling", "fallen"],
    ["falling", "fallin"],
    ["falling", "falln"],
    ["telling", "tellin"],
    ["something", "somthin"],
]

class Rule_Creole_Ending_In_Ing_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Ending_In_Ing_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule