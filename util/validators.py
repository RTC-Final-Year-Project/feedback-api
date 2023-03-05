from marshmallow import Schema, fields, validate, pre_load

class FeedBackRequestInputSchema(Schema):
    # string with at least 1 char
    spelling_word = fields.Str(required=True, validate=validate.Length(min=1))
    attempted_spelling = fields.Str(required=True, validate=validate.Length(min=1))
    student_id = fields.Str(required=True, validate=validate.Length(min=1))
    # at least 5 years old
    student_age = fields.Int(required=True, validate=validate.Range(min=5))

    @pre_load
    def slugify_name(self, in_data, **kwargs):
        in_data["spelling_word"] = in_data["spelling_word"].strip()
        in_data["attempted_spelling"] = in_data["attempted_spelling"].strip()
        in_data["student_id"] = in_data["student_id"].strip()
        return in_data
    
class FeedBackRequestInputException(Exception):
    """Raised when the input json does not match expected schema"""