# Class 1
class Animal:
    """
    Parent class.
    """
# need a class attribute.

    def __init__(self, name, species, age = 1):
        self.name = name
        self.species = species
        self.age = age

    def eat(self):
        print(f'{self.name} has been fed')

    def gets_old(self):
        self.age += 1
        if (self.age > 0 and self.age <= 2):
            print(f'{self.name} celebrated a birthday!')
        elif(self.age > 3):
            print(f'{self.name} celebrated a birthday! it is now a mature {self.species} ')

    def describe_self(self):
        print(f'Hello my name is {self.name}, I am a {self.age} years old {self.species}')
        
