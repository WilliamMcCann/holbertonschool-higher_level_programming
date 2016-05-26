'''describes a TaskModel class'''
class TaskModel():

    def __init__(self, title):
        if title == None or not str:
            raise Exception("title not valid")
        self.__title = title

    def callback_title(self):
        return self.__callback_title

    def get_title(self):
        return self.title

    def set_callback_title(self, func):
        return func

    def toggle(self):
        return ''.join(t[i] for i in range(len(t) - 1, -1, -1))

    def __str__(self):
        return title
