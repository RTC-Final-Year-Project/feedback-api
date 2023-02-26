from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Ending_In_D_G_E


rule = Rule_Ending_In_D_G_E

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["judge", "judge"],
    ["edge", "edge"],
    ["porridge", "porridge"],
    ["rummage", "rummidge"],
    ["fridge", "fridge"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["judge", "jage"],
    ["judge", "juge"],
    ["judge", "jug"],
    ["judge", "judg"],
]

class Rule_Ending_In_D_G_E_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Ending_In_D_G_E_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule