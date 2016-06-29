'''orders array'''

import threading

class OrderedArray():

    def __init__(self):

    list = []
    ordered_numbers_threads = []

    def add(self, number):
        try:
           val = int(number)
        except ValueError:
           print("number is not an integer")
        self.number = val

        ordered_numbers = OrderedArrayThread(self.number)
        OrderedArray.ordered_numbers_threads += [ordered_numbers]
        ordered_numbers.start()

        for o in OrderedArray.ordered_numbers_threads:
            o.join()

    def isSorting(self):
        for ordered_numbers in OrderedArray.ordered_numbers_threads:
            return ordered_numbers.isAlive()

    def __str__(self):
        return str(OrderedArray.list)

class OrderedArrayThread(threading.Thread):

    def __init__(self, number):
        try:
           val = int(number)
        except ValueError:
           print("number is not an integer")
        self.number = val

    def run(self):
        OrderedArray.list += self.number
        OrderedArray.list.sort()
