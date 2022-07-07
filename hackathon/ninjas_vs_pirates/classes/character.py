class Character:
    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , attacke):
        attacke.health -= self.strength
        print(f"{attacke.name} - HP: {attacke.health}\n")
        return self

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        is_battling = False
    
    def battle(self):
        while(self.p1.health > 0 and self.p2.health > 0):
            is_battling = True
            self.p1.attack(self.p2)
            self.p2.attack(self.p1)
        else:
            if(self.p1.health == 0):
                print(f"Game Over: {self.p1.name} lost the battle.")
            else:
                print(f"Game Over: {self.p2.name} lost the battle.")
            is_battling = False
        return self
