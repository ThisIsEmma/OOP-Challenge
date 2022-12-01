# Class 2
from animal import Animal


class Lion(Animal):
    location = 'Toronto zoo '
    """
    This class inherits from the parent Animal class.
    We can override the init and other methods.
    """

    def __init__(self, name, species, age, is_hungry = True, dangerous=True):
        super().__init__(name, species, age, is_hungry)
        self.dangerous = dangerous

    def eat(self):
        super(Lion, self).eat()
        print('it ate all the meat and gained 1 lb.')
        self.is_hungry = False

    #modify class attribute
    @classmethod
    def move(cls, new_location):
        cls.location = new_location
        print(f'All lions have been moved to {new_location}')

    #overrides superclass method
    def describe_self(self):
        if (self.dangerous):
         print(f'{self.name} is a dangerous {self.species}, beware!')
        else: 
         print(f'{self.name} is an affective {self.species}, come pet it')


# run from the terminal;

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    simba = Lion('Simba', 'African Lion', 1)
    sunny = Lion('Sunny', 'Indian feline', 4, False)

    lions = [simba, sunny]

    for lion in lions:
        lion.describe_self()
        lion.eat()

    Lion.move('Vancouver')