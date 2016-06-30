'''manages a store class and how many customers and items it has'''

from random import randint
from time import sleep
import threading

class Store():
    def __init__(self, item_number, person_capacity):
        self.item_number = item_number
        self.person_capacity = person_capacity
        self.semaphore = threading.BoundedSemaphore(self.person_capacity)

    def enter(self):
        self.semaphore.acquire()

    def buy(self):
        sleep(randint(5,10))
        if self.item_number >= 0 :
            self.item_number -= 1
        if self.item_number < 0:
            return False
        self.semaphore.release()
        return True
