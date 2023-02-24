from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Change_Y_To_I_Exception

rule = Rule_Change_Y_To_I_Exception

combinations_that_follow_rule = combinations_ignore_rule = [
    ["flier", "flier"], 
    ["uglier", "uglier"], 
    ["relied", "relied"],
    ["funniest", "funniest"],
    ["tries", "tries"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["uglier", "uglyer"], 
    ["flier", "flyer"], 
    ["uglier", "uglyer"], 
    ["relied", "relyed"],
    ["funniest", "funnyest"],
    ["tries", "tryes"],
]

class Rule_Change_Y_To_I_Exception_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Change_Y_To_I_Exception_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule