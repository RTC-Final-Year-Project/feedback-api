from .determine_spelling_violation import determine_violated_rule, determine_violated_rules
from .generate_spelling_feedback import determine_feedback, process_corrective_feedback
from .spelling_history import get_student_action_list


class FeedbackModule():
    def check_spelling(self, spelling_word, attempted_spelling, student_id, student_age):
        if spelling_word.strip() == "" or attempted_spelling.strip() == "":
            return None
        
        violated_rule = determine_violated_rule(spelling_word, attempted_spelling)
        
        feedback = determine_feedback(violated_rule)
        
        return dict(
            spelling_word=spelling_word,
            attempted_spelling=attempted_spelling,
            student_id=student_id,
            num_word_attempts = 2,
            attempt_id = 4,
            emotive_feedback = feedback
        )
    
    def analyze_spelling(self, spelling_word, attempted_spelling, student_id, student_age):
        if spelling_word.strip() == "" or attempted_spelling.strip() == "":
            return None
        
        violated_rules = determine_violated_rules(spelling_word, attempted_spelling)

        student_action_list = get_student_action_list(student_id)

        session_id = 9
        corrective_feedback = process_corrective_feedback(session_id, spelling_word, attempted_spelling, violated_rules, student_id, student_age, student_action_list)
        
        return dict(
            spelling_word=spelling_word,
            attempted_spelling=attempted_spelling,
            student_id=student_id,
            num_word_attempts = 2,
            attempt_id = 4,
            emotive_feedback = corrective_feedback
        )
        
        
        