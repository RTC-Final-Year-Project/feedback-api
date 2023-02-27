from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Th_Stopping_T

rule = Rule_Creole_Th_Stopping_T

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["thing", "thing"],
    ["thin", "thin"],
    ["earth", "earth"],
    ["birth", "birth"],
    ["thank", "thank"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["thing", "ting"],
    ["thin", "tin"],
    ["earth", "eart"],
    ["birth", "bert"],
    ["birth", "birt"],
    ["thank", "tank"],
]

class Rule_Creole_Th_Stopping_T_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Th_Stopping_T_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule