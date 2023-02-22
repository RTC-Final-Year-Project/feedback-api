from .AssessTestCases import AssessTestCases

from feedback_module.spelling_rules import Rule_V_J_K_W_X_never_doubled

rule = Rule_V_J_K_W_X_never_doubled

combinations_that_follow_rule = combinations_ignore_rule = [#bookkeeper ?
    ["hello", "world"],
    ["vivid", "vivid"],
    ["justify", "justify"],
    ["kebab", "kebab"],
    ["awkward", "awkward"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["vivid", "vivvid"],
    ["justify", "jjustify"],
    ["kebab", "kkebab"],
    ["awkward", "awwkward"],
]



class Rule_V_J_K_W_X_never_doubled_Unit_Tests(AssessTestCases.UnitTestCases):
    rule = rule
    combinations_that_follow_rule = combinations_that_follow_rule
    combinations_that_violate_rule = combinations_that_violate_rule

class Rule_V_J_K_W_X_never_doubled_Integration_Tests(AssessTestCases.IntegrationTestCases):
    rule = rule
    combinations_ignore_rule = combinations_ignore_rule
    combinations_detect_rule = combinations_detect_rule