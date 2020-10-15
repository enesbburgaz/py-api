from flask import Flask,render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    response = requests.get('http://api.open-notify.org/astros.json')
    return response.status_code


if __name__ == '__main':
    app.run(debug=True)