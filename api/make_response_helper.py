import json
from flask import Flask,make_response
from .data import data
import json

app = Flask(__name__)

@app.route('/')
def cityList():
    content = json.dumps(data())
    response = make_response(content, 200, {'Content-Type': 'application/json'})
    return response