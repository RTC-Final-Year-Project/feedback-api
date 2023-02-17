# from determine_violated_rule import determine_violated_rule
# from test_rules import *


# def main():
#     word_attempts = dict(
#         buying=["buyying", "buying", "adioje"],
#         delayed=["delayd", "delaid", "delayed"],
#         churches=["churchs", "churches"],
#         lives=["lifes", "livs", "lives"],
#         excess=["exsess", "excess"],
#         knives=["knifes", "knives", "knifs"],
#         receive=["receive", "recieve", "conceive", "concieve"],
#         conceive=["receive", "recieve", "conceive", "concieve"],
#         retrieve=["receive", "retrieve", "retreive"],
#         quick=["qick", "uqick", "qwick", "kwik",
#                "kwick", "quik", "qwic", "quick"],
#         Qatar=["Quatar", "kata", "katar", "catar", "Quata", "Qatar"],
#         Trinidad=["trinidad", "trinedad", "Trinidad"],
#         Max=["max", "macks", "maxs", "Max"],
#         judge=["jug", "judg", "juge", "juj", "juje", "judj", "judge"],
#         hive=["hiv", "hyve", "highv", "hyve", "hive"],
#         bake=["backe", "bayk", "beyk", "bake"],
#         clock=["cluck", "clok", "cluk", "clock"],
#         donkey=["donki", "donke", "dunkey",
#                 "donkii", "donkie", "donky", "donkey"],
#         money=["moni", "mone", "mony", "monny", "monney", "money"],
#         lucky=["luky", "lucy", "locky", "locki",
#                "luki", "lucke", "lucki", "lucky"],
#         asking=["askin", "askn", "asken", "asking"],
#         they=["dey", "day", "they"],
#         together=["togedah", "toogeda", "together"],
#         whether=["whedah", "weather", "weda", "whether"]
#     )

#     for word in word_attempts:
#         # break;
#         for attempt in word_attempts[word]:
#             violated_rule = determine_violated_rule(word, attempt)

#             feedback = ""

#             if violated_rule == None:
#                 feedback = "That is correct!"
#             elif violated_rule.id == -1:
#                 feedback = "Spelling Violation Not Found"
#             else:
#                 feedback = violated_rule.rule

#             print(word + " - " + attempt + ": " + str(feedback) + "\n")

#     Test_Rule_Ending_Vowel_and_Y_Add_Suffix_Ed_Ing_Only()

# # main()
