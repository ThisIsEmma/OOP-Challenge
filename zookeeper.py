class ZooKeeper:
    def __init__(self, name, zoo=None):
        self.name = name
        self.zoo = zoo

    def feed_animals(self):
        if not self.zoo:
            return "Not currently working at a zoo."

        if not self.zoo.animals:
            print("There are no animals to feed. ")

        for animal in self.zoo.animals:
            if animal.hungry:
                animal.eat()

    def show_off_animal(self, animal):
        print(f"Hello, today I'd like to show you {animal.name}.")
        print(f"{animal.name} is a {animal.species} and {animal.age} years old.")
