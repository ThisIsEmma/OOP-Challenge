from zookeeper import ZooKeeper


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
        print(f"{zookeeper.name} has just joined {self.name}")


if __name__ == "__main__":

    central_park_zoo = Zoo(
        "Central Park Zoo", "East 64th Street, New York, NY 10021, United States"
    )

    print(central_park_zoo.ticket_price)
    Zoo.change_ticket_price(30)
    print(central_park_zoo.ticket_price)
    central_park_zoo.give_information()
    andrew = ZooKeeper("Andrew", central_park_zoo)
    andrew.feed_animals()
