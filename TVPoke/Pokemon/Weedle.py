from TVPoke.BaseClasses.PokeTypes import Poison
from TVPoke.BaseClasses.Move import Move

class Weedle(Poison):
    def __init__(self):
        moves = [
            Move("Posion Sting", "NORMAL", 15),
            Move("String Shot ", "FIRE", 0),
            Move("Shield Dust [does nothing]", "NORMAL", 0),
            Move("Splash [does nothing]", "WATER", 0)
        ]
        super().__init__("Weedle", 40, moves, "./TVPoke/Pokemon/imgs/Weedle.png")