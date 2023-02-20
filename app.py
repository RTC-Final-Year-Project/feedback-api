from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin  # cors

from feedback_module import FeedbackModule

FM = FeedbackModule()

def create_app(config={}):
    app = Flask(__name__)
    CORS(app)
    return app

# API Route
app = create_app()

@app.route("/", methods=["GET"])
# @cross_origin #cors
def index_page():
    return "Hello world"


@app.route("/feedback", methods=["POST"])
# @cross_origin #cors
def handle_feedback():
    data = request.json # get data from form submission
    
    spelling_word = data.get("spelling_word")
    attempted_spelling = data.get("attempted_spelling")
    student_id = data.get("student_id")
    student_age = data.get("student_age")
    
    # TODO check all data is legitimate before calling function below
    
    response = FM.check_spelling(spelling_word, attempted_spelling, student_id, student_age)

    return jsonify(response)
