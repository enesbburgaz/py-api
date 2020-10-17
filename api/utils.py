JSON_MIME_TYPE = 'application/json'

def searchCity(data, city):
    for i in data:
        if i['stateName'] == city:
            return i