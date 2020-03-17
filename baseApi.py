import requests
import json

class baseApi:

    def __init__(self):
        self.URL = 'https://restcountries.eu/rest/v2/name/'


    def connection(self):
        api_url = self.URL
        response = requests.get(api_url)

        if response.status_code == 200:
            return True
        else:
            return False

    def getCountryInfo(self,country):
        api_url = self.URL+country
        response = requests.get(api_url)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            return None
