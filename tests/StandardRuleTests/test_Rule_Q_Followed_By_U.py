from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Q_Followed_By_U


rule = Rule_Q_Followed_By_U

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["earthquake", "earthquake"],
    ["quick", "kwick"],
    ["quick", "qucki"],
    ["quick", "quik"],
    ["quail", "kwale"],
    ["quick", "cwick"],
    ["quick", "kwiq"],
    ["niqab", "niqab"],
    ["niqab", "niquab"],
    ["Qatar", "Qatar"],
    ["Qatar", "Quatar"],
    ["unique", "unik"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["quick", "qwic"],
    ["earthquake", "earthqwake"],
    ["unique", "uniqe"],
    ["queen", "qween"],
    ["quail", "qwhale"],
    ["quail", "qwhale"],
    ["quail", "qwail"],
]

class Rule_Q_Followed_By_U_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Q_Followed_By_U_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule