def generate_feedback(violated_rule, student_age=10, attempts_history={}):
    feedback = ""

    if violated_rule == None:
        feedback = "That is correct!"
    elif violated_rule.id == -1:
        feedback = "Please sound out the word and try again."
    else:
        feedback = violated_rule.definition

    return feedback

def generate_corrective_feedback(violated_rule, student_age = 10, attempts_history=[]):
    feedback = "" 