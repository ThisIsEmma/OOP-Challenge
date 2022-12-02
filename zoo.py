from zookeeper import ZooKeeper
from lion import Lion
from deer import Deer


class Zoo:
    ticket_price = 20

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animals = list()
        self.zookeepers = list()

    @classmethod
    def change_ticket_price(cls, price):
        cls.ticket_price = price

    def give_information(self):
        print(
            f"Welcome to {self.name}.\nWe current house {len(self.animals)} animals.\nWe are located at {self.location}."
        )

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the zoo!")

    def add_zookeeper(self, zookeeper):
        self.zookeepers.append(zookeeper)
        zookeeper.zoo = self
        print(f"{zookeeper.name} has just joined {self.name}")


if __name__ == "__main__":
    # Zoo instance
    central_park_zoo = Zoo(
        "Central Park Zoo", "East 64th Street, New York, NY 10021, United States"
    )

    # Animal instances
    bambi = Deer("Bambi", "white-tailed deer", 1, True, False)
    simba = Lion("Simba", "lion", 2, True, False)

    # ZooKeeper instances
    andrew = ZooKeeper("Andrew Pham")
    edith = ZooKeeper("Edith Sakatia")

    central_park_zoo.add_animal(bambi)
    central_park_zoo.add_animal(simba)
    central_park_zoo.add_zookeeper(andrew)

    andrew.feed_animals()
    edith.feed_animals()

    andrew.show_off_animals()
