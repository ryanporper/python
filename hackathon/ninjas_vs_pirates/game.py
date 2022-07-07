from classes.ninja import Ninja
from classes.pirate import Pirate
from classes.character import Game

michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")

g1 = Game(michelangelo, jack_sparrow)
g1.battle()
