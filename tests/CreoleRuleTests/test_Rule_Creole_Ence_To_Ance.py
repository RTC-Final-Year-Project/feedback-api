from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Ence_To_Ance

rule = Rule_Creole_Ence_To_Ance

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["conference", "conference"],
    ["experience", "experience"],
    ["independence", "independence"],
    ["audience", "audience"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
   ["conference", "conferance"],
    ["experience", "experiance"],
    ["independence", "independance"],
    ["audience", "audiance"],
]

class Rule_Creole_Ence_To_Ance_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Ence_To_Ance_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule