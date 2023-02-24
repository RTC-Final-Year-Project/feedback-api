from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from App.routes import index_routes

routes = [
    index_routes
]

def add_routes(app, routes):
    for route in routes:
        app.register_blueprint(route)

def loadConfig(app, config):
    app.config["ENV"] = os.environ.get("ENV", "DEVELOPMENT")
    if app.config["ENV"] == "DEVELOPMENT":
        app.config.from_object("App.config")
    else:
        app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
        app.config["DEBUG"] = os.environ.get("ENV").upper() != "PRODUCTION"
        app.config["ENV"] = os.environ.get("ENV")
        
    for key, value in config.items():
        app.config[key] = config[key]

def create_app(config={}):
    app = Flask(__name__)
    CORS(app)
    loadConfig(app, config)
    app.config['PREFERRED_URL_SCHEME'] = "https"    
    add_routes(app, routes)
    return app