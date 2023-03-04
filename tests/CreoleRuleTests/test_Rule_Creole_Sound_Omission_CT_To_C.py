from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Sound_Omission_CT_To_C

rule = Rule_Creole_Sound_Omission_CT_To_C

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["impact", "impact"],
    ["respect", "respect"],
    ["connect", "connect"],
    ["react", "react"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["impact", "impac"],
    ["respect", "respec"],
    ["connect", "connec"],
    ["react", "reac"],
]

class Rule_Creole_Sound_Omission_CT_To_C_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Sound_Omission_CT_To_C_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule