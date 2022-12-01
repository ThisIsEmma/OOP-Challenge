# Class 2
from animal import Animal


class Lion(Animal):
    """
    This class inherits from the parent Animal class.
    We can override the init and other methods.
    """

    def __init__(self, name, species, age, dangerous=True):
        super().__init__(name, species, age)
        self.dangerous = dangerous
