import math

'''describes a Circle class'''
class Circle():
    def __init__(self, radius):
        self.__radius = radius

    def get_color(self):
            return self.__color

    def set_color(self, color):
            self.__color = color

    def get_center(self):
            return self.__center

    def set_center(self, center):
            self.__center = center

    def area(self):
            return ((math.pi) * (self.__radius ** 2))
