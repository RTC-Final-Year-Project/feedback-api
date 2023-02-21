from flask import Flask, request, jsonify
from flask_cors import CORS
from util.validators import FeedBackRequestInputSchema, FeedBackRequestInputException
import json

feedback_request_input_schema = FeedBackRequestInputSchema()

from feedback_module import FeedbackModule

FM = FeedbackModule()

def create_app(config={}):
    app = Flask(__name__)
    CORS(app)
    return app

# API Route
app = create_app()

@app.route("/", methods=["GET"])
def index_page():
    return "Hello world"


@app.route("/feedback", methods=["POST"])
def handle_feedback():
    try:
        data = request.json # get data from form submission
        
        # validate request json
        json_errors = feedback_request_input_schema.validate(data)
        if json_errors:
            raise FeedBackRequestInputException(json_errors)
        
        # process json data
        spelling_word = data.get("spelling_word")
        attempted_spelling = data.get("attempted_spelling")
        student_id = data.get("student_id")
        student_age = data.get("student_age")        
        
        # check spelling
        response = FM.check_spelling(spelling_word, attempted_spelling, student_id, student_age)

        return jsonify(response), 200
    except FeedBackRequestInputException as err:
        json_error = json.loads(str(json_errors).replace("\'", "\""))
        print("Feedback request error occured", json_error)
        return jsonify(json_error), 400
    except Exception as e:
        print("An error occured", e)
        err_msg = dict(messsage = "An unexpected error occured. Please try again.")
        return jsonify(err_msg), 400
