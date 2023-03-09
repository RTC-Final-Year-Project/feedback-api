from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Own_To_Ong

rule = Rule_Creole_Own_To_Ong

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["down", "down"],
    ["town", "town"],
    ["bound", "bound"],
    ["bound", "bong"],
    ["own", "own"],
    ["downtown", "downtown"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["down", "dong"],
    ["town", "tong"],
    ["down", "dung"],
    ["town", "tung"],
    ["brown", "brong"],
    ["brown", "brung"],
    ["downtown", "dongtong"],
    ["downtown", "dongtown"],
    ["downtown", "downtong"],
    ["downtown", "dontong"],
    ["downtown", "dungtong"],
    ["downtown", "dungtown"],
    ["downtown", "downtung"],
    ["downtown", "duntung"],
]

class Rule_Creole_Own_To_Ong_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Own_To_Ong_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule