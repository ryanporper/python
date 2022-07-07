from classes.character import Character

class Ninja(Character):
    def __init__( self , name ):
        super().__init__(name)
        self.strength = 10
        self.speed = 4