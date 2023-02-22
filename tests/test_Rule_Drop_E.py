from .AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_Drop_E

rule = Rule_Drop_E

combinations_that_follow_rule = combinations_ignore_rule = [
    ["riding", "riding"],
    ["loving", "loving"],
    ["driver", "driver"],
    ["statement", "statement"],
    ["livable", "livable"],
    ["dotage", "dotage"],
    ["inspired", "inspired"],
    ["truest", "truest"],
    ["adulteration", "adulteration"],
    ["celebratory", "celebratory"],
    ["famous", "famous"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["arguing", "argueing"],
    ["riding", "rideing"],
    ["loving", "loveing"],
]



class Rule_Drop_E_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_Drop_E_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule