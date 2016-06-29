'''prints to argv[2] file name an argv[1] number of lorem ipsum paragraphs'''
import threading
import requests

class LoripsumThread(threading.Thread):
    def __init__(self, filename):
        threading.Thread.__init__(self)

        self.__filename = filename

    def run(self):
        file = open(self.__filename, 'a')
        r = requests.get('http://loripsum.net/api/1/short')
        file.write(r.text.encode('utf-8'))
        file.close()
