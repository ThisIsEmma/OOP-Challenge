from animal import Animal


class Deer(Animal):
    location = 'Toronto zoo '
    """
    This class inherits from the parent Animal class.
    We can override the init and other methods.
    """

    def __init__(self, name, species, age, antlers = False):
        super().__init__(name, species, age)
        self.antlers = antlers

    def eat(self):
        super(Deer, self).eat()
        print('it ate all the herbs and gained 0.5 lb.')

    #modify class attribute
    @classmethod
    def move(cls, new_location):
        cls.location = new_location
        print(f'All deers have been moved to {new_location}')

    #overrides superclass method
    def describe_self(self):
        if (self.antlers):
         print(f'{self.name} is a {self.species} deer with beautiful antlers')
        else: 
         print(f'{self.name} is a {self.species} deer with no antlers yet...')


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