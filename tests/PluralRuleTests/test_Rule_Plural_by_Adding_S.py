from ..AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Plural_By_Adding_S

rule = Rule_Plural_By_Adding_S

combinations_that_follow_rule = combinations_ignore_rule = [
    ["plans", "plans"],
    ["begins", "begins"],
    ["dogs", "dogs"],
    ["cats", "cats"],
    ["cars", "casr"],
    ["cups", "cups"],
    ["vans", "car"]
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["plans", "planz"],
    ["dogs", "dog"],
    ["cats", "catce"],
    ["cups", "cupz"]
]



class Rule_Plural_By_Adding_S_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Plural_By_Adding_S_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule