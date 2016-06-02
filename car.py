import json

class Car:
    def __init__(self, *args, **kwargs):

        if len(args) > 0 and isinstance(args[0], dict):

            hash = args[0]
            name = hash.get('name')
            brand = hash.get('brand')
            nb_doors = hash.get('nb_doors')
        else:
            name = kwargs.get('name')
            brand = kwargs.get('brand')
            nb_doors = kwargs.get('nb_doors')

        if name == None or not isinstance(name, str):
            raise Exception("name is not a string")
        self.__name = name
        if brand == None or not isinstance(brand, str):
            raise Exception("brand is not a string")
        self.__brand = brand
        if nb_doors <= 0 or not isinstance(nb_doors, int):
            raise Exception("nb_doors is not > 0")
        self.__nb_doors = nb_doors

    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand

    def get_nb_doors(self):
        return self.__nb_doors

    def to_hash(self):
        return { 'name': self.__name,
                'brand': self.__brand,
                'nb_doors': self.__nb_doors}

    def __str__(self):
        return "%s %s (%d)" % (self.__name, self.__brand, self.__nb_doors)

    def set_nb_doors(self, number):
        self.__nb_doors = number

    def to_json_string(self):
        return json.dumps(self.to_hash())
