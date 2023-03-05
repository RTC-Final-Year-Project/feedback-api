from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Change_Y_To_I_Unless_Vowel_Before

rule = Rule_Change_Y_To_I_Unless_Vowel_Before

combinations_that_follow_rule = combinations_ignore_rule = [
    ["joyful", "world"],
    ["happiness", "happyness"],
    ["buying", "buying"],
    ["crying", "criing"],
    ["trying", "trying"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["joyful", "joiful"],
    ["player", "plaier"],
]

class Rule_Change_Y_To_I_Unless_Vowel_Before_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Change_Y_To_I_Unless_Vowel_Before_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule