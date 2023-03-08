from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Y_Before_A_Sound

rule = Rule_Creole_Y_Before_A_Sound

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["carrot", "carrot"],
    ["cat", "cat"],
    ["garden", "garden"],
    ["gas", "gas"],
    ["garlic", "garlic"],
    ["yarn", "yarn"],
    ["Priya", "Priya"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["carrot", "cyarrot"],
    ["cat", "cyat"],
    ["garden", "gyarden"],
    ["gas", "gyas"],
    ["garlic", "gyarlic"],
    ["carrot", "cyarot"],
    ["garden", "gyadin"],
]

class Rule_Creole_Y_Before_A_Sound_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Y_Before_A_Sound_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule