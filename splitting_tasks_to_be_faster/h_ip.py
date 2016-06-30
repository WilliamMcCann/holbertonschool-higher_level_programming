import threading
import requests
import json

class IPThread(threading.Thread):
    def __init__(self, ip, callback):
        threading.Thread.__init__(self)

        self.__ip = ip
        self.__callback = callback

    def run(self):
        r = requests.get('https://api.ip2country.info/ip?' + str(self.__ip))
        obj = json.loads(r.text)
        self.__callback(obj.get('countryName').encode('utf-8'))
        print "Search: " + str(self.__ip)
        print "countryName: " + obj.get('countryName').encode('utf-8')
