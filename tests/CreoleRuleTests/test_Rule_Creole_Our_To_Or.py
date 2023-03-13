from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Our_To_Or

rule = Rule_Creole_Our_To_Or

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["colour", "colour"],
    ["favourite", "favourite"],
    ["favour", "favour"],
    ["honour", "honour"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["colour", "color"],
    ["favourite", "favorite"],
    ["favour", "favor"],
    ["honour", "honor"],
]

class Rule_Creole_Our_To_Or_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Our_To_Or_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule