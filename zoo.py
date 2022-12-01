from zookeeper import ZooKeeper


class Zoo:
    """
    Will be composed of Animal/ZooKeeper instances
    """

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animals = list()
        self.zookeepers = list()

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the zoo!")

    def add_zookeeper(self, zookeeper):
        self.zookeepers.append(zookeeper)
        print(f"{zookeeper.name} has just joined {self.name}")


if __name__ == "__main__":

    central_park_zoo = Zoo(
        "Central Park Zoo", "East 64th Street, New York, NY 10021, United States"
    )
    andrew = ZooKeeper("Andrew", central_park_zoo)
    andrew.feed_animals()
