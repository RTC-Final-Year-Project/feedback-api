import unittest
from os import listdir
from os.path import isfile, join
from feedback_module.spelling_rules import rules_list

strip_string = "feedback_module.spelling_rules."

class Rules_Meta_Integration_Tests(unittest.TestCase):
    def test_all_rule_files_added_to_list(self):
        spelling_rules_path = "./feedback_module/spelling_rules/"
        files_list = [f for f in listdir(spelling_rules_path) if isfile(join(spelling_rules_path, f))]
        rule_files = list(filter(lambda filename: filename.startswith("Rule_"), files_list))
        rule_names_from_files = list(map(lambda rulename: rulename[:-3], rule_files))

        rule_names_from_lists = list(map(lambda ruleclass: ruleclass.__name__[len(strip_string) if ruleclass.__name__.startswith(strip_string) else 0:], rules_list))

        all_created_rules_added_to_list = set(rule_names_from_files) == set(rule_names_from_lists)
        
        if not all_created_rules_added_to_list:
            unadded_rules = list(set(rule_names_from_files) ^ set(rule_names_from_lists))
            print("\n - ".join(["The following created rules have not been added to the rules list:\n"] + unadded_rules) + "\n")
            
        assert all_created_rules_added_to_list
    
    def test_all_rule_class_names_match_file_names(self):
        rule_names_from_lists = list(map(lambda ruleclass: ruleclass.__name__, rules_list))
        
        unmatched_classes = list(map(lambda rule_name: rule_name[len(strip_string):], list(filter(lambda filename: filename.startswith(strip_string), rule_names_from_lists))))
        
        if unmatched_classes:
            print("\n - ".join(["The following rule files do not have classes with matching names:\n"] + unmatched_classes) + "\n")

        assert not unmatched_classes