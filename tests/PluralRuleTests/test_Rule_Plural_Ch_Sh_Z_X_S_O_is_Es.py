from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Plural_Ch_Sh_Z_X_S_O_is_Es


rule = Rule_Plural_Ch_Sh_Z_X_S_O_is_Es

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["churches", "churches"],
    ["brushes", "brushes"],
    ["watches", "watches"],
    ["foxes", "foxes"],
    ["echoes", "echoes"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["churches", "churchs"],
    ["brushes", "brushs"],
    ["watches", "watchs"],
    ["foxes", "foxe"],
    ["echoes", "echos"],
]

class Rule_Plural_Ch_Sh_Z_X_S_O_is_Es_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Plural_Ch_Sh_Z_X_S_O_is_Es_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule