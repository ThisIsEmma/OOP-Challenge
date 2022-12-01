from animal import Animal


class Deer(Animal):
    location = 'Toronto zoo '
    """
    This class inherits from the parent Animal class.
    We can override the init and other methods.
    """

    def __init__(self, name, species, age, is_hungry = True, antlers = False):
        super().__init__(name, species, is_hungry,  age)
        self.antlers = antlers

    def eat(self):
        super(Deer, self).eat()
        print('it ate all the herbs and gained 0.5 lb.')
        self.is_hungry = False

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
    woody = Deer('woody', 'purple giant', 1)
    skinny = Deer('skinny', 'rare ruminant', 4)

    deers = [woody, skinny]

    for deer in deers:
        deer.describe_self()
        deer.eat()
        print(deer.is_hungry)

    Deer.move('Vancouver Zoo')