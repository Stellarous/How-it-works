class Cat:
    pass

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("{self.name} says WOOOOOOOF!")

    @classmethod
    def get_species(cls):
        return cls.species

my_dog = Dog("Fido", "Labrador")
my_dog.bark()
