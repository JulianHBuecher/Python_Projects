# Usages of classes in Python
# For object oriented programming in Python

# Creating a class Presenter
class Presenter():
    # Constructor
    # The keyword "self" is just like "this" from other programming languages
    # It gives you access to the current instance of the object
    def __init__(self, name):
        # Self.Name is just a property
        self.name = name
    # Method
    def say_hello(self):
        print("Hello, " + self.name)

p1 = Presenter("Julian")
# The fields could be updated on the fly
p1.name = "Empty"
p1.say_hello()

def print_greeting(name: str) -> str:
    return print("Hello " + name)

# Lore for Classes in Python 
# Accessibility in Python
# -> Everything is public
# Conventions for suggesting accessibility
# _ means avoid unless you really know what you're doing
# __ (double underscore) means do not use

# Another possibility to create a class and control the accesibility
class PrivatePresenter():
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        print("In the Getter")
        return self.__name
    @name.setter
    def name(self, value):
        # validation happens here
        # here some validation for null values or empty strings could be created
        self.__name = value
    # Method
    def say_hello(self):
        print("Hello, " + self.name)

p2 = PrivatePresenter("Maximilian")
p2.say_hello()