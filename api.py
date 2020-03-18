import socket

import flask
from baseApi import baseApi
from flask import jsonify
import requests
import json
from flask_restful import Resource

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def gettingInfo(country):
    baseApiObj = baseApi()
    country = country
    countryInfo = None
    countryInfo = baseApiObj.getCountryInfo(country)
    return countryInfo


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hello</h1>'''


@app.route('/<title1>/')
def getAll(title1=None):
    countryinfo = gettingInfo(title1)
    if countryinfo is not None:
        return str(countryinfo)
    else:
        return 'ERROR NOT FOUUUUUND'


@app.route('/<title1>Info=<spec>/', methods=['GET'])
def getBySpec1(title1, spec):
    spec = spec
    countryInfo = None
    countryInfo = gettingInfo(title1)
    if countryInfo is not None:
        return (spec + "=" + str(countryInfo[0][spec]))
    else:
        return 'not Fouuuuund'


@app.route('/<title1>/<spec1>/<spec2>', methods=['GET'])
def getBySpec2(title1, spec1, spec2):
    spec1 = spec1
    spec2 = spec2
    countryInfo = None
    countryInfo = gettingInfo(title1)

    if countryInfo is not None:
        return (spec1 + "=" + str(countryInfo[0][spec1]) + " , " + spec2 + "=" + str(countryInfo[0][spec2]))
    else:
        return 'NOT FOUUNNNDD'


app.run()
