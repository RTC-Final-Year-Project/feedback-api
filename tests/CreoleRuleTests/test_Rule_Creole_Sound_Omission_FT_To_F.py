from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Sound_Omission_FT_To_F

rule = Rule_Creole_Sound_Omission_FT_To_F

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["craft", "craft"],
    ["soft", "soft"],
    ["drift", "drift"],
    ["gift", "gift"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["craft", "craf"],
    ["soft", "sof"],
    ["drift", "drif"],
    ["gift", "gif"],
]

class Rule_Creole_Sound_Omission_FT_To_F_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Sound_Omission_FT_To_F_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule