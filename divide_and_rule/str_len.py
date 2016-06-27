'''add the length of word to the class attribute total_str_length'''

import threading
import sys

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
        

words = sys.argv[1:]
str_length_threads = []

StrLengthThread.total_str_length = len(words) - 1
for word in words:
    str_length_thread = StrLengthThread(word)
    str_length_threads += [str_length_thread]
    str_length_thread.start()

for t in str_length_threads:
    t.join()

print "%d" % StrLengthThread.total_str_length
