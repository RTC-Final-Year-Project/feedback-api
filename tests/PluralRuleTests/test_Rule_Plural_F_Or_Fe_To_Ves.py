from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Plural_F_Or_Fe_To_Ves


rule = Rule_Plural_F_Or_Fe_To_Ves

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["queen", "queen"],
    ["knives", "knives"],
    ["lives", "lives"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["lives", "lifes"],
    ["lives", "livs"],
    ["knives", "knifes"],
    ["knives", "knifs"],
]

class Rule_Plural_F_Or_Fe_To_Ves_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Plural_F_Or_Fe_To_Ves_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule