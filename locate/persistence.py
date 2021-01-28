import requests
import json


class ParseJSON(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)


def getdatabyCity(city: str):
    url = "https://geo.api.gouv.fr/communes?nom=" + city

    # url = url + city
    res = requests.get(url)
    result = json.loads(res.content)
    for item in result:
        # print (item['nom'])
        if item['nom'].lower() == city.lower():
            return item
    return "No match"


print(getdatabyCity('Paris'))
