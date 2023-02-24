from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Q_Followed_By_U_Exception


rule = Rule_Q_Followed_By_U_Exception

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["queen", "queen"],
    ["quick", "kwick"],
    ["earthquake", "earthquake"],
    ["quick", "qucki"],
    ["quick", "quik"],
    ["quick", "quik"],
    ["Qatar", "kata"],
    ["Qatar", "catar"],
    ["niqab", "nikab"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["Qatar", "Quatar"],
    ["niqab", "niquab"],
    ["Qatar", "Quata"],
]

class Rule_Q_Followed_By_U_Exception_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Q_Followed_By_U_Exception_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule