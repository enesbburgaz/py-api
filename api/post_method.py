import json
from flask import Flask, Response, request, jsonify
from .data import data
places = data()
app = Flask(__name__)

@app.route("/")
def index():
    return 'Python Flask Web Api'

@app.route('/api/v1/places/all')
def getAll():
    return jsonify(data())

@app.route('/api/v1/places/add', methods=['POST'])
def placeAdd():
    place = {
    "title": "Kent Park - Sakarya",
    "description": "Yesillik.",
    "id": "kentparksakarya",
    "images": [],
    "stateName": "sakarya",
    "type": "Park",
    "address": "Serdivan yolu uzeri",
    "location": {
      "lat": 0,
      "long": 0
    }}
    places.append(place)
    return jsonify({'places': place})
