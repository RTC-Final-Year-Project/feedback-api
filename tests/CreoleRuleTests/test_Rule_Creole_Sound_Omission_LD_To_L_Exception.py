from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Sound_Omission_LD_To_L_Exception

rule = Rule_Creole_Sound_Omission_LD_To_L_Exception

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["gold", "gold"],
    ["shield", "shield"],
    ["guild", "guild"],
    ["mild", "mild"],
    ["fold", "fold"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["gold", "gole"],
    ["shield", "shiele"],
    ["guild", "guile"],
    ["mild", "mile"],
    ["fold", "fole"],
    ["child", "chile"],
]

class Rule_Creole_Sound_Omission_LD_To_L_Exception_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Sound_Omission_LD_To_L_Exception_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule