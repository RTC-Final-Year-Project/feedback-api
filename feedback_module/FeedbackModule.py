from .determine_spelling_violation import determine_violated_rule
from .generate_spelling_feedback import generate_feedback


class FeedbackModule():
    def check_spelling(self, spelling_word, attempted_spelling, student_id, student_age):
        
        violated_rule = determine_violated_rule(spelling_word, attempted_spelling)
        
        feedback = generate_feedback(violated_rule)
        
        return dict(
            spelling_word=spelling_word,
            attempted_spelling=attempted_spelling,
            student_id=student_id,
            num_word_attempts = 2,
            attempt_id = 4,
            emotive_feedback = feedback
        )
        
        