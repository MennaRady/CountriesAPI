import requests
import json
import requests_cache

class baseApi:

    requests_cache.install_cache('country_caches', backend='memory', expire_after=300)

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
        print (response.from_cache)

        if response.status_code == 200:
            return (json.loads(response.content), response.from_cache)

        else:
            return None
