from datetime import datetime
import json
import itertools

'''describes a Person class'''
class Person():
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        if id < 0 or not int:
            raise Exception("id is not an integer")
        self.__id = id
        if first_name == " " or not str:
            raise Exception("string is not a string")
        self.__first_name = first_name
        self.last_name = " "
        if len(date_of_birth) is not 3 and all(isinstance(n, int) for n in date_of_birth):
            raise Exception("date_of_birth is not a valid date")
        self.__date_of_birth = date_of_birth
        if genre not in Person.GENRES or not str:
            raise Exception("genre is not valid")
        self.__genre = genre
        if eyes_color not in Person.EYES_COLORS or not str:
            raise Exception("eyes_color is not valid")
        self.__eyes_color = eyes_color

    def get_id(self):
        return self.__id

    def get_eyes_color(self):
        return self.__eyes_color

    def get_genre(self):
        return self.__genre

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_first_name(self):
        return self.__first_name

    def __str__(self):
        return "%s %s" % (self.__first_name, self.last_name)

    def is_male(self):
        if genre is "Male":
            return True

    def age(self):
        today = [5, 20, 2016]
        return today[2] - self.__date_of_birth[2] - ((today[0], today[2]) < (self.__date_of_birth[0], self.__date_of_birth[1]))
'''JSON for Task 3'''

    def json(self):
        dictionary = {
        'id':self.__id,
        'eyes_color':self.__eyes_color,
        'genre':self.__genre,
        'date_of_birth':self.__date_of_birth,
        'first_name':self.__first_name,
        'last_name':self.last_name,
        'kind':self.__class
        }
        return dictionary

    def load_from_json(self, json):
        if json is not hash:
            raise Exception("json is not valid")
        self.__id = json['id']
        self.__eyes_color = json['eyes_color']
        self.__genre = json['genre']
        self.__date_of_birth = json['date_of_birth']
        self.__first_name = json['first_name']
        self.last_name = json['last_name']
        type(x).__name__ = json['kind']


'''describes child classes of Person'''
class Baby(Person):

    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return True

    def can_vote(self):
        return False

class Teenager(Person):

    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return True

    def can_vote(self):
        return False

class Adult(Person):

    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return False

    def can_vote(self):
        return True

class Senior(Person):

    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return False

    def can_vote(self):
        return True

'''two new functions for Task Three'''

def save_to_file(list, filename):
    with open('list') as data_file:
        data = json.dumps(data_file)
    with open('filename', 'w') as outfile:
        json.loads(data, outfile)

def load_from_file(filename):
    if filename == " " or not str:
        raise Exception("filename is not valid or doesn't exist")
    with open (filename, 'a+') as input:
        more_data = json.dumps(input)
