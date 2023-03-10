def ldifference(string1, string2):
    min_len = min(len(string1), len(string2)) 
    for i in range(min_len):
        if string1[i] != string2[i]:
            return [i, (string1[i], string2[i])]
    if len(string1) > len(string2):
        return [len(string2), (string1[len(string2)], None)]
    elif len(string1) < len(string2):
        return [len(string1), (None, string2[len(string1)])]

    return [-1, (None, None)]

def rdifference(string1, string2):
    if len(string1) > len(string2):
        return [len(string2), (string1[len(string2)], None)]
    elif len(string1) < len(string2):
        return [len(string1), (None, string2[len(string1)])]
    for i in reversed(range(len(string2))):
        if string1[i] != string2[i]:
            return [i, (string1[i], string2[i])]
    return [-1, (None, None)]       
      
def samedifference(string1, string2):
    left_diff = ldifference(string1, string2)
    right_diff = rdifference(string1, string2)
    
    if left_diff == right_diff:
        return left_diff
    return [-1, (None, None)]

# backward difference
def bdifference(string1, string2):
    min_len = min(len(string1), len(string2))
    for i in range(min_len):
        char1 = string1[len(string1) - i - 1]
        char2 = string2[len(string2) - i - 1]
        if char1 != char2:
            return [i, (char1, char2)]
    if len(string1) > len(string2):
        return [len(string2), (string1[len(string1) - len(string2) - 1], None)]
    elif len(string1) < len(string2):
        return [len(string1), (None, string2[len(string2) - len(string1) - 1])]

    return [-1, (None, None)]

def decapitalize_first_letter(sentence):
  return "".join([sentence[:1].lower(), sentence[1:]]) 