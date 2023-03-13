from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Word_Shortening

rule = Rule_Creole_Word_Shortening

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["trickery", "trickery"],
    ["library", "library"],
    ["primary", "primary"],
    ["boundary", "boundary"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["trickery", "trickry"],
    ["library", "libry"],
    ["primary", "primry"],
    ["boundary", "boundry"],
]

class Rule_Creole_Word_Shortening_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Word_Shortening_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule