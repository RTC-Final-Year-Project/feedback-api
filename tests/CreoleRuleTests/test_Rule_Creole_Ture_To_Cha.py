from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Ture_To_Cha

rule = Rule_Creole_Ture_To_Cha

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["picture", "picture"],
    ["feature", "feature"],
    ["literature", "literature"],
    ["sculpture", "sculpture"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["picture", "pickcha"],
    ["picture", "piccha"],
    ["feature", "feacha"],
    ["feature", "feecha"],
    ["literature", "literacha"],
    ["sculpture", "sculpcha"],
]

class Rule_Creole_Ture_To_Cha_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Ture_To_Cha_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule