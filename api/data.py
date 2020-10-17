import json

def data():
    f = open('places.json')
    data = json.load(f)
    return data