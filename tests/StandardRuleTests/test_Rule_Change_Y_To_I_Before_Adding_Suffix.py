from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Change_Y_To_I_Before_Adding_Suffix

rule = Rule_Change_Y_To_I_Before_Adding_Suffix

combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["happiness", "happiness"],
    ["buying", "buying"],
    ["crying", "criing"],
    ["trying", "trying"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["easiest", "easyest"],
    ["happiness", "happyness"],
    ["cried", "cryed"],
    # ["trying", "triing"],
]

class Rule_Change_Y_To_I_Before_Adding_Suffix_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Change_Y_To_I_Before_Adding_Suffix_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule