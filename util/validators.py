from marshmallow import Schema, fields, validate

class FeedBackRequestInputSchema(Schema):
    # string with at least 1 char
    spelling_word = fields.Str(required=True, validate=validate.Length(min=1))
    attempted_spelling = fields.Str(required=True, validate=validate.Length(min=1))
    student_id = fields.Str(required=True, validate=validate.Length(min=1))
    # at least 5 years old
    student_age = fields.Int(required=True, validate=validate.Range(min=5))
    
class FeedBackRequestInputException(Exception):
    """Raised when the input json does not match expected schema"""