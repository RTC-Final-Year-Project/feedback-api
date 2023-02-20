import unittest

from feedback_module.determine_spelling_violation import determine_violated_rule

class AssessTestCases():
    class UnitTestCases(unittest.TestCase):
        rule = ""
        combinations_that_follow_rule = ""
        combinations_that_violate_rule = ""
        
        def test_unit_rule_combinations(self):
            """
            this method accepts two lists:
            - the list of combinations that should follow this rule
            - the list of combinations that should violate this rule
            
            this method fails assertion on 2 conditions:
            - the list of combinations that should follow this rule had some combinations that did not follow this rule
            - the list of combinations that should violate this rule had some combinations that did not violate this rule
            """
            
            if not self.rule or not self.combinations_that_follow_rule or not self.combinations_that_violate_rule:
                assert True
                return 
            
            failed_to_follow_list = []
            for combination in self.combinations_that_follow_rule:
                rule_followed = self.rule.check_if_followed(combination[0], combination[1])
                if rule_followed == False:
                    failed_to_follow_list.append(combination[0] + "-" + combination[1])
            
            failed_to_violate_list = []
            for combination in self.combinations_that_violate_rule:
                rule_followed = self.rule.check_if_followed(combination[0], combination[1])
                if rule_followed == True:
                    failed_to_violate_list.append(combination[0] + "-" + combination[1])
                
            combinations_follow_rule = len(failed_to_follow_list) == 0
            combinations_violate_rule = len(failed_to_violate_list) == 0
            
            if not combinations_follow_rule:
                print("\n - ".join([self.rule.__name__ + " unit test failed for words that are supposed to follow rule:\n"] + failed_to_follow_list) + "\n")
            
            if not combinations_violate_rule:
                print("\n - ".join([self.rule.__name__ + " unit test failed for words that are supposed to violate rule:\n"] + failed_to_violate_list) + "\n")
                
            assert combinations_follow_rule == True
            assert combinations_violate_rule == True
            
    class IntegrationTestCases(unittest.TestCase):
        rule = ""
        combinations_ignore_rule = ""
        combinations_detect_rule = ""
        def test_integration_rule_combinations(self):
            """
            this method accepts two lists:
            - the list of combinations that should follow this rule (thus making it be ignored by the system function)
            - the list of combinations that should violate this rule (thus making it be detected by the system function)
            
            this method fails assertion on 2 conditions:
            - the list of combinations that should ignore this rule had some combinations that did not ignore this rule
            - the list of combinations that should detect this rule had some combinations that did not detect this rule
            """
            
            if not self.rule or not self.combinations_ignore_rule or not self.combinations_detect_rule:
                assert True
                return 
            
            failed_to_follow_list = []
            for combination in self.combinations_ignore_rule:
                obtained_rule = determine_violated_rule(combination[0], combination[1])
                if obtained_rule == self.rule:
                    failed_to_follow_list.append(combination[0] + "-" + combination[1])
            
            failed_to_violate_list = []
            for combination in self.combinations_detect_rule:
                obtained_rule = determine_violated_rule(combination[0], combination[1])
                if obtained_rule != self.rule:
                    failed_to_violate_list.append(combination[0] + "-" + combination[1])
            
            combinations_follow_rule = len(failed_to_follow_list) == 0
            combinations_violate_rule = len(failed_to_violate_list) == 0
            
            if not combinations_follow_rule:
                print(self.rule.__name__ + " integration test failed for words that are supposed to ignore this rule: " + "\n".join(failed_to_follow_list))
            if not combinations_violate_rule:
                print("\n".join(self.rule.__name__ + " integration test failed for words that are supposed to detect this rule: " + failed_to_violate_list) + "\n")
                    
            assert combinations_follow_rule == True
            assert combinations_violate_rule == True