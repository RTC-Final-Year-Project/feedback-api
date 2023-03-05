from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Sound_Omission_PT_To_P

rule = Rule_Creole_Sound_Omission_PT_To_P

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["adapt", "adapt"],
    ["accept", "accept"],
    ["disrupt", "disrupt"],
    ["intercept", "intercept"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["adapt", "adap"],
    ["accept", "accep"],
    ["disrupt", "disrup"],
    ["intercept", "intercep"],
]

class Rule_Creole_Sound_Omission_PT_To_P_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Sound_Omission_PT_To_P_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule