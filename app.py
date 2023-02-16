from flask import Flask
from flask_cors import CORS, cross_origin #cors


app = Flask(__name__)
CORS(app)

#API Route

@app.route("/", methods=["GET"])
# @cross_origin #cors
def index_page():
    return "Hello world"

@app.route("/feedback", methods=["POST"])
# @cross_origin #cors
def handle_feedback():
    return "Feedback world"

if __name__ == "__main__":
    app.run(debug=True)