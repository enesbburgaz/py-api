from flask.globals import session
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    session = requests.Session()
    response = session.get('http://google.com')
    return session.cookies.get_dict()