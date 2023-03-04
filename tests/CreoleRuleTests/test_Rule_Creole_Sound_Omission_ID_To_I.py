from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Sound_Omission_ID_To_I

rule = Rule_Creole_Sound_Omission_ID_To_I

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["acid", "acid"],
    ["candid", "candid"],
    ["hybrid", "hybrid"],
    ["solid", "solid"],
    ["stupid", "stupid"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["acid", "aci"],
    ["candid", "candi"],
    ["hybrid", "hybri"],
    ["solid", "soli"],
    ["stupid", "stupi"],
]

class Rule_Creole_Sound_Omission_ID_To_I_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Sound_Omission_ID_To_I_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule