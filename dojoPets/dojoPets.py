class Pet:

    def __init__(self, name , type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    def make_noise(self):
        print(self.noise)
        return self



class Ninja:
    def __init__(self, first_name, last_name , treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print(f"Walking {self.pet.name}")
        return self

    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("You ran out of pet food, oh no!")
        return self

    def bathe(self):
        self.pet.make_noise()
        return self

treats = ['Bone','Bacon',"Peanutbutter"]
pet_food = ['Chicken','Burger']

barky = Pet("Barky","Dog",['barks a lot','is loud'],"Bark Bark")

dylan = Ninja("Dylan","Dingle",treats,pet_food, barky)

dylan.feed().walk().bathe()












# class Ninja:
#     def __init__(self, first_name, last_name, pet, treats, pet_food):
#         self.first_name = first_name
#         self.last_lame = last_name
#         self.pet = pet
#         self.treats = treats
#         self.pet_food = pet_food

#     def walk(self):
#         print("Walking pet")
#         self.pet.play()
#         return self

#     def feed(self):
#         print("Feeding pet")
#         if len(self.pet_food) > 0:
#             food = self.pet_food.pop()
#             print(f"Feeding {self.pet.name} {food}!")
#             self.pet.eat()
#         else:
#             print("No more pet food!!")
#         return self
    
#     def bathe(self):
#         print("Bathing pet they seem happy")
#         self.pet.noise()
#         return self

# class Pet:
#     def __init__(self, name, type, tricks, noise):
#         self.name = name
#         self.type = type
#         self.tricks = tricks
#         self.health = 100
#         self.energy = 50
#         self.noise = noise


#     def sleep(self):
#         print("sleeping")
#         self.energy += 25
#         return self
    
#     def eat(self):
#         print("eating")
#         self.energy += 5
#         self.health += 10
#         return self

#     def play(self):
#         print("playingggg")
#         self.health += 5
#         self.energy -= 25
#         return self

#     def noise(self):
#         print(self.noise)
#         return self

# treats = ["bacon", "pigear", "peanutbutter"]    
# da_pet_food = ["chicken", "burger"]

# barky = Pet("Barky", "Dog",['barks a lot, is loud'], "Bark bark")

# dylan = Ninja("Dylan", "Lyle", treats, da_pet_food, barky)

# dylan.feed()
# dylan.feed()
# dylan.feed()