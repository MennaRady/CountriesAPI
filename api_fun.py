from baseApi import baseApi


class apiLogic:

    def gettingInfo(self, country):
        baseApiObj = baseApi()
        countryInfo = baseApiObj.getCountryInfo(country)
        return countryInfo

    def spec1(self, countryInfo, spec):
        return (spec + "=" + str(countryInfo[0][spec]))

    def spec2(self, countryInfo, spec1, spec2):
        return (spec1 + "=" + str(countryInfo[0][spec1]) + " , " + spec2 + "=" + str(countryInfo[0][spec2]))
