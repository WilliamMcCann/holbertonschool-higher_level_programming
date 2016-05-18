'''describes a Square class'''
class Square():
    def __init__(self, side_length):
        self.__side_length = side_length

    def get_color(self):
            return self.__color

    def set_color(self, color):
            self.__color = color

    def get_center(self):
            return self.__center

    def set_center(self, center):
            self.__center = center

    def area(self):
            return (self.__side_length * self.__side_length)

    def __call__(self):
            ('*' * self.__side_length)
            for i in range((self.__side_length - 2)):
                ('*' + ' ' * (self.__side_length - 2) + '*')
            ('*' * self.__side_length)

    def s():
            return "test"
