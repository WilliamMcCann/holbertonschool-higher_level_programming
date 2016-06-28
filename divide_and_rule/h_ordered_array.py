'''orders array'''

import threading

class OrderedArray():

    def __init__(self):

    list = []

    def add(self, number):
        try:
           val = int(number)
        except ValueError:
           print("number is not an integer")
        self.number = val

        add number to the list correctly sorted. The sort action should be done in a thread OrderedArrayThread

    def isSorting(self):
        return True if some threads from the function add are not finished
        use isAlive() for this

        return str(list)

class OrderedArrayThread(threading.Thread):

    def __init__(self, number):
        try:
           val = int(number)
        except ValueError:
           print("number is not an integer")
        self.number = val
    
