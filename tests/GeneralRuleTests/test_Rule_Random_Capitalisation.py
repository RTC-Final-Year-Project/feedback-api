from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Random_Capitalisation


rule = Rule_Random_Capitalisation

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["Elizabeth", "Elizabeth"],
    ["London", "London"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["Elizabeth", "EliZaBeth"],
    ["London", "LuNdun"],
    ["Trinidad", "TriNiDad"],
    ["hello", "heLO"],
    ["duck", "dUUck"],
    ["queen", "qUEEN"],
    ["queen", "qUEN"],
    ["queen", "qUEEEN"],
]

class Rule_Random_Capitalisation_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Random_Capitalisation_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule