from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Start_With_Capital_Letter


rule = Rule_Start_With_Capital_Letter

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["Elizabeth", "Elizabeth"],
    ["London", "London"],
    ["Trinidad", "TriNidad"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["Elizabeth", "elizabeth"],
    ["London", "lundun"],
    ["Trinidad", "triNiDad"],
    ["hello", "Hello"],
    ["duck", "Dock"],
]

class Rule_Start_With_Capital_Letter_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Start_With_Capital_Letter_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule