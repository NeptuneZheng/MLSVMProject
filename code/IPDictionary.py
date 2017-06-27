import requests
import json

def getIPCity(ip):
    url="http://ip-api.com/json/"+ip
    res=requests.get(url)
    resStr = res.text

    jsonStr = json.loads(resStr)

    IPCity = jsonStr["country"]+"/"+jsonStr["regionName"]+"/"+jsonStr["city"]

    # for ["MACAO","TAIWAN","HONG KONG"] country should be "CHINA"
    if(jsonStr["country"] in ["MACAO","TAIWAN","HONG KONG"]):
        IPCity="CHINA/"+jsonStr["country"]+"/"+jsonStr["regionName"]

    # print(IPCity)
    return IPCity

# getIPCity("145.253.172.234")