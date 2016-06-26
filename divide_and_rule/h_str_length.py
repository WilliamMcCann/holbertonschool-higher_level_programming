'''add the length of word to the class attribute total_str_length'''

import threading

class StrLengthThread(threading.Thread):

    total_str_length = 0

    def __init__(self, word):
        threading.Thread.__init__(self)
        try:
           val = str(word)
        except ValueError:
           print("word is not a string")
        self.word = val

    def run(self):
        a = len(self.word)
        StrLengthThread.total_str_length = StrLengthThread.total_str_length + a
