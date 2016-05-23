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
        self.last_name = last_name
            raise Exception("date_of_birth is not a valid date")
        self.__date_of_birth = date_of_birth
        if genre not in Person.GENRES or not str:
            raise Exception("genre is not valid")
        self.__genre = genre
        if eyes_color not in Person.EYES_COLORS or not str:
            raise Exception("eyes_color is not valid")
        self.__eyes_color = eyes_color
        self.is_married_to = is_married_to

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

    def is_married_to (int):
        return p.id

    '''JSON for Task 3'''

    def json(self):
        dictionary = {
        'id':self.__id,
        'eyes_color':self.__eyes_color,
        'genre':self.__genre,
        'date_of_birth':self.__date_of_birth,
        'first_name':self.__first_name,
        'last_name':self.last_name,
        'kind':self.__class__.__name__,
        'is_married_to':self.is_married_to
        }
        return dictionary

    def load_from_json(self, json):
        if type(json) is not dict:
            raise Exception("json is not valid")
        self.__id = json['id']
        self.__eyes_color = json['eyes_color']
        self.__genre = json['genre']
        self.__date_of_birth = json['date_of_birth']
        self.__first_name = json['first_name']
        self.last_name = json['last_name']
        self.is_married_to = json['is_married_to']

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

    def can_be_married(self):
        return False

    def is_married(self):
        if is_married_to is not None:
            return True

    def divorce(self, p):
         self.is_married_to = 0
         p.is_married_to = 0

    def just_married_with(self, p):
        if self.is_married_to is not 0 or p.is_married_to is not 0:
            raise Exception("Already married")
        if self.can_be_married is False or p.can_be_married is False:
            raise Exception("Can't be married")
        else:
            self.is_married_to = p.id
            p.is_married_to = self.id
            if self.genre == Female:
                self.last_name = p.last_name

class Teenager(Person):

    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return True

    def can_vote(self):
        return False

    def can_be_married(self):
        return False

    def is_married(self):
        if is_married_to is not None:
            return True

    def divorce(self, p):
         self.is_married_to = 0
         p.is_married_to = 0

class Adult(Person):

    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True

    def is_married(self):
        if is_married_to is not None:
            return True

    def divorce(self, p):
         self.is_married_to = 0
         p.is_married_to = 0

class Senior(Person):

    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True

    def is_married(self):
        if is_married_to is not None:
            return True

    def divorce(self, p):
         self.is_married_to = 0
         p.is_married_to = 0

'''two new functions for Task Three'''

def save_to_file(list, filename):
    list_json = []
    for i in list:
        list_json.append(i.json())
    with open(filename, 'w') as outfile:
        json.dump(list_json, outfile)

def load_from_file(filename):
    with open(filename) as outfile:
        data = json.load(outfile)
    # here, data is a list of hash, now you have to convert to Person or Baby... class`
    list = []
    for i in data:
        if i['kind'] == "Baby":
            p = Baby(1, "Sam", [1, 1, 2000], "Male", "Green") # default values`
        if i['kind'] == "Senior":
            p = Senior(1, "Sam", [1, 1, 2000], "Male", "Green") # default values`
        if i['kind'] == "Teenager":
            p = Teenager(1, "Sam", [1, 1, 2000], "Male", "Green") # default values`
        if i['kind'] == "Adult":
            p = Adult(1, "Sam", [1, 1, 2000], "Male", "Green") # default values`
        else:
            p = Person(1, "Sam", [1, 1, 2000], "Male", "Green") # default values`
        p.load_from_json(i)
        list.append(p)
    return list
