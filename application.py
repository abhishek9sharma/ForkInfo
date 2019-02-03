from flask import Flask
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"