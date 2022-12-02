class ZooKeeper:
    def __init__(self, name):
        self.name = name
        self.zoo = None

    def feed_animals(self):
        if not self.zoo:
            print("Not currently working at a zoo.")
            return

        if not self.zoo.animals:
            print("There are no animals to feed. ")

        for animal in self.zoo.animals:
            if animal.is_hungry:
                animal.eat()

    def show_off_animals(self):
        if self.zoo:
            for animal in self.zoo.animals:
                animal.describe_self()
