import threading
import requests

class IPThread(threading.Thread):
    def __init__(self, ip, callback):

        self.__ip = ip
        self.__callback = callback

    def run(self):
        r = requests.get('https://api.ip2country.info/' + str(self.__ip))
        self.__callback("r")
