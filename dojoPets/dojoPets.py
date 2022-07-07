class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_lame = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        print("Walking pet")
        return self

    def feed(self):
        print("Feeding pet")
        return self
    
    def bathe(self):
        print("Bathing pet")
        return self

class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        health = 100
        energy = 50

    def sleep(self):
        print("sleeping")
        return self
    
    def eat(self):
        print("eating")
        return self

    def play(self):
        print("playingggg")
        return self

    def noise(self):
        print("bark bark")
        return self
        