from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (55, 118, 171))

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        
    def elementsToDisplay(self):
        self.elements = [Image((50, 50), 100, 100, "./imgs/feild.jpg" )]

        y = 0
        #two rows of three
        for trainer in self.trainers:
            x = 0
            y += 100/3
            for poke in trainer.pokemon:
                x += 100/4
                self.elements.append(Image((x, y), 20, 20, poke.img))
                self.elements.append(Label((x, y + 10), 20, 10, poke.name))
        x = 15
        y = 80
        for move in self.trainers[0].pokemon[0].moves:
            self.elements.append(Label((x, y), 20, 10, move.name))
            y -= 15
            
                                

#"./TVPoke_26/img/feild.jpg"  