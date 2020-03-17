import flask
from flask import jsonify
import requests
import json
from flask_restful import Resource

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hello</h1>'''

@app.route('/<title1>/<title2>/<title3>/<title4>', methods=['GET'])
def getAll(title1, title2, title3, title4):
    response = requests.get('https://restcountries.eu/rest/v2/all')
    return response.json()[0]


app.run()
