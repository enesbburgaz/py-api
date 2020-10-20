from flask import Flask,jsonify,abort
import requests
import json
from api.utils import JSON_MIME_TYPE,searchCity
from .data import data

app = Flask(__name__)

@app.route("/")
def index():
    return 'Python Flask Web Api'

@app.route('/api/v1/places/all')
def getAll():
    return jsonify(data())

@app.route('/api/v1/places/<string:city>')
def getCurrentCity(city):
    currentData = searchCity(data(), city)
    if currentData is None:
        abort(404)
    content = json.dumps(currentData)
    return content, 200, {'Content-Type': JSON_MIME_TYPE}