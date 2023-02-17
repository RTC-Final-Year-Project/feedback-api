def generate_feedback(violated_rule, student_age=10, attempts_history={}):
    feedback = ""

    if violated_rule == None:
        feedback = "That is correct!"
    elif violated_rule.id == -1:
        feedback = "Spelling Violation Not Found"
    else:
        feedback = violated_rule.rule

    return feedback
