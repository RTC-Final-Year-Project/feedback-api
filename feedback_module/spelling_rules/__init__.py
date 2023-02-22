from .Rule_Plural_F_Or_Fe_To_Ves import *
from .Rule_Plural_Ch_Sh_Z_X_S_O_is_Es import *
from .Rule_I_E_Except_C import *
from .Rule_S_Never_Follows_X import *
from .Rule_Ending_Vowel_and_Y_Add_Suffix_Ed_Ing_Only import *
from .Rule_Q_Followed_By_U import *
from .Rule_Q_Followed_By_U_Exception import *
from .Rule_Start_With_Capital_Letter import *
from .Rule_Ending_In_V_Or_J import *
from .Rule_Ending_In_D_G_E import *
from .Rule_CK import *
from .Rule_K import *
from .Rule_Ending_In_E_Y import *
from .Rule_Creole_Ending_In_I_N_G import *
from .Rule_Creole_Th_Stopping import *
# from .Rule_Creole_Th_Stopping_D import *
# from .Rule_Creole_Th_Stopping_T import *
from .Rule_Last_Consonant_Is_Doubled import *
from .Rule_Plural_By_Adding_S import *
from .Rule_Drop_E import *
from .Rule_Change_Y_To_I import *
from .Rule_Change_Y_To_I_Exception import *
from .Rule_V_J_K_W_X_never_doubled import *

rules_list = [
  Rule_Plural_F_Or_Fe_To_Ves,
  Rule_Plural_Ch_Sh_Z_X_S_O_is_Es,
  Rule_I_E_Except_C,
  Rule_S_Never_Follows_X,
  Rule_Ending_Vowel_and_Y_Add_Suffix_Ed_Ing_Only,
  Rule_Q_Followed_By_U,
  Rule_Q_Followed_By_U_Exception,
  Rule_Start_With_Capital_Letter,
  Rule_Ending_In_V_Or_J,
  Rule_Ending_In_D_G_E,
  Rule_CK,
  Rule_K,
  Rule_Ending_In_E_Y,
  Rule_Creole_Ending_In_I_N_G,
  Rule_Creole_Th_Stopping,
  # Rule_Creole_Th_Stopping_D,
  # Rule_Creole_Th_Stopping_T,
  Rule_Last_Consonant_Is_Doubled,
  Rule_Plural_By_Adding_S,
  Rule_Drop_E,
  Rule_Change_Y_To_I,
  Rule_Change_Y_To_I_Exception,
  Rule_V_J_K_W_X_never_doubled,
]

# check for one letter off: [receive: receiv]
# check for some letters in between off: [receive: retrieve]
# try to design for adding arbitrary rules
# read rules from file