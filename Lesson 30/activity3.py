# Class 1
class India():
    def capital(self):
        print("New Delhi is the capital of India. ")

    def language(self):
        print("Hindi is the most widely spoken language of India. ")

    def type(self):
        print("India is a developing country.")

# Class 2
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA. ")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country. ")

# Class 3
class Bangladesh():
    def capital(self):
        print("Dhaka is the capital of Bangladesh. ")

    def language(self):
        print("Bangla is the primary language of Bangladesh.")

    def type(self):
        print("Bangladesh is a developing country. ")

# Object Creation
obj_ind = India()
obj_usa = USA()
obj_bd = Bangladesh()

# Common Interface
for country in (obj_ind, obj_usa, obj_bd):
    country.capital()
    country.language()
    country.type()