from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_CE_Sound_Like_S


rule = Rule_CE_Sound_Like_S

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["peace", "peace"],
    ["piece", "piece"],
    ["fleece", "fleece"],
    ["sentence", "sentence"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["peace", "peas"],
    ["piece", "pies"],
    ["fleece", "flees"],
    ["sentence", "sentens"],
]

class Rule_CE_Sound_Like_S_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_CE_Sound_Like_S_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule