from classes.character import Character

class Pirate(Character):
    def __init__( self , name ):
        super().__init__(name)
        self.strength = 5
        self.speed = 3

