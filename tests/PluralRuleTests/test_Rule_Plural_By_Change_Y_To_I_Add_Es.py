from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Plural_By_Change_Y_To_I_Add_Es

rule = Rule_Plural_By_Change_Y_To_I_Add_Es

combinations_that_follow_rule = combinations_ignore_rule = [
    ["cities", "cities"],
    ["parties", "parties"],
    ["babies", "babies"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["cities", "citys"],
    ["parties", "partys"],
]



class Rule_Plural_By_Change_Y_To_I_Add_Es_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Plural_By_Change_Y_To_I_Add_Es_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule