class Animal:
    def __init__(self, name, species, age=1, is_hungry=True):
        self.name = name
        self.species = species
        self.age = age
        self.is_hungry = is_hungry

    def eat(self):
        print(f"{self.name} has been fed")
        self.is_hungry = False

    def gets_old(self):
        self.age += 1
        if self.age > 0 and self.age <= 2:
            print(f"{self.name} celebrated a birthday!")
        elif self.age > 3:
            print(
                f"{self.name} celebrated a birthday! it is now a mature {self.species} "
            )

    def describe_self(self):
        print(
            f"Hello my name is {self.name}, I am a {self.age} years old {self.species}"
        )


if __name__ == "__main__":
    carnivores = Animal("Carnivore", "feline")
    herbivores = Animal("Herbivores", "ruminant")

    carnivores.eat()
    herbivores.eat()
