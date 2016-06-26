'''prints out the Fibonacci number for a given input'''

import threading

class FibonacciThread(threading.Thread):

    def __init__(self, number):
        threading.Thread.__init__(self)
        try:
           val = int(number)
        except ValueError:
           print("number is not an integer")
        self.number = val

    def run(self):
        a = 0
        b = 1
        for i in range(0, self.number):
        	temp = a
        	a = b
        	b = temp + b
        print(str(self.number) + "=>" + str(a))
