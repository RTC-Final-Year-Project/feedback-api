from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Th_Stopping_D

rule = Rule_Creole_Th_Stopping_D

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["there", "there"],
    ["father", "father"],
    ["together", "together"],
    ["them", "them"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["there", "deer"],
    ["there", "dere"],
    ["the", "de"],
    ["father", "fada"],
    ["together", "togeder"],
    ["together", "togeda"],
    ["them", "dem"],
]

class Rule_Creole_Th_Stopping_D_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Th_Stopping_D_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule