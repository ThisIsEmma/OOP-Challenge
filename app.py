# Class 1
class Animal:
    """
    Parent class.
    """

    def __init__(self, name, species, age):
        pass


# Class 2
class Lion(Animal):
    """
    This class inherits from the parent Animal class.
    We can override the init and other methods.
    """

    def __init__(self, name, species, age, dangerous=True):
        super().__init__(name, species, age)
        self.dangerous = dangerous


# Class 3
class ZooKeeper:
    """ """

    def __init__(self, name, zoo):
        pass

    def feed_animals(self):
        pass

    def check_health(self):
        pass


# Class 4
class Zoo:
    """
    Will be composed of Animal/ZooKeeper instances
    """

    def __init__(self, name, location):
        self.animals = list()
        self.zookeepers = list()
        pass

    def add_animal(self, animal):
        pass

    def add_zookeeper(self, zookeeper):
        pass
