'''append to sentence the word reversed with after a space'''

import threading

class ReverseStrThread(threading.Thread):

    sentence = " "

    def __init__(self, word):
        threading.Thread.__init__(self)
        try:
           val = str(word)
        except ValueError:
           print("word is not a string")
        self.word = val

    def run(self):
        a = self.word[::-1] + " "
        ReverseStrThread.sentence = ReverseStrThread.sentence + a
