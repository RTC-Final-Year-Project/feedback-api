import unittest

from feedback_module.spelling_rules import Rule_CK

from .asses_rules import assess_unit_rule_combinations
from .asses_rules import assess_integration_rule_combinations

rule = Rule_CK

# the list of combinations that are supposed to follow this rule (thus being ignored by the module checker because isFollowed = True)
combinations_that_follow_rule = combinations_ignore_rule = [
    ["hello", "world"],
    ["duck", "dock"],
    ["clock", "clock"],
    ["quick", "qucki"],
]

# the list of combinations that are supposed to violate this rule (thus being detected by the module checker because isFollowed = False)
combinations_that_violate_rule = combinations_detect_rule = [
    ["quick", "quic"],
    ["clock", "clok"],
    ["lucky", "luky"],
]

class Rule_CK_Unit_Tests(unittest.TestCase):
    def test_rule_correctness(self):
        assess_unit_rule_combinations(rule, combinations_that_follow_rule, combinations_that_violate_rule)
    
class Rule_CK_Integration_Tests(unittest.TestCase):
    def test_rule_integration(self):
        assess_integration_rule_combinations(rule, combinations_ignore_rule, combinations_detect_rule)