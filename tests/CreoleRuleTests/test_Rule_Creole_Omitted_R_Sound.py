from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Creole_Omitted_R_Sound

rule = Rule_Creole_Omitted_R_Sound

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["teacher", "teacher"],
    ["preacher", "preacher"],
    ["work", "work"],
    ["short", "short"],
    ["ear", "ear"],
    ["garlic", "garlic"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["teacher", "teacha"],
    ["preacher", "preacha"],
    ["work", "wok"],
    ["short", "shot"],
    ["short", "shawt"],
    ["fear", "feah"],
    ["fear", "feh"],
    ["garlic", "galic"],
]

class Rule_Creole_Omitted_R_Sound_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Creole_Omitted_R_Sound_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule