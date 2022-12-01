# Class 3
class ZooKeeper:
    """
    Will take in a Zoo instance.
    """

    def __init__(self, name, zoo):
        self.name = name
        self.zoo = zoo

    def feed_animals(self):

        if not self.zoo.animals:
            print("There are no animals to feed. ")

        for animal in self.zoo.animals:
            if animal.hungry:
                animal.eat()

    def check_health(self):
        pass
