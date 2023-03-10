from .spelling_rules import (rules_list, Rule)


def determine_violated_rule(actual_word, attempted_word):
  if actual_word == attempted_word:
    return None
  
  if actual_word.strip() == "" or attempted_word.strip() == "":
    return Rule

  for rule in rules_list:
    rule_followed = rule.check_if_followed(actual_word, attempted_word)
    if rule_followed == False:
      return rule

  return Rule
