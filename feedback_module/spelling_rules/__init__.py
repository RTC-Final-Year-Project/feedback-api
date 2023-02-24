from .Rule import *
from .PluralRules import *
from .CreoleRules import *
from .GeneralRules import *
from .StandardRules import *

rules_list = [
  *standard_rules_list,
  *general_rules_list,
  *plural_rules_list,
  *creole_rules_list,
]

# check for one letter off: [receive: receiv]
# check for some letters in between off: [receive: retrieve]
# try to design for adding arbitrary rules
# read rules from file