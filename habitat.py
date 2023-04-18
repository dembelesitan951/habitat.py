class Animal:
    def __init__(self, name, species, habitat):
        self.name = name
        self.species = species
        self.habitat = habitat


class Dog(Animal):
    def __init__(self, name, breed, habitat):
        super().__init__(name, species="Dog",
