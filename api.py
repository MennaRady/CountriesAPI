import flask
import api_fun
from api_fun import apiLogic

app = flask.Flask(__name__)
app.config["DEBUG"] = True






@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hello</h1>'''


@app.route('/<title1>/')
def getAll(title1=None):
    api_funob = apiLogic()
    countryinfo =api_funob.gettingInfo(title1)
    if countryinfo is not None:
        return str(countryinfo)
    else:
        return 'ERROR NOT FOUUUUUND'




@app.route('/<title1>/info=<spec>/', methods=['GET'])
def getBySpec1(title1, spec):
    api = apiLogic()
    countryInfo = api.gettingInfo(title1)
    return api.spec1(countryInfo,spec)

@app.route('/<title1>/info=<spec1>,<spec2>/', methods=['GET'])
def getBySpec2(title1, spec1, spec2):
    api = apiLogic()
    countryInfo = api.gettingInfo(title1)
    return api.spec2(countryInfo,spec1,spec2)




app.run()
