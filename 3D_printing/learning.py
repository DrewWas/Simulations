import os
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import *

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        properties = WindowProperties()
        properties.setSize(1000,700)
        self.win.requestProperties(properties) 



        self.environment = loader.loadModel("Models/environment")
        self.environment.reparentTo(render)
			
        self.tempActor = Actor("Models/panda-model", {"walk" : "Models/panda-model_run"})
        self.tempActor.reparentTo(render)
        self.tempActor.setPos(0,7,0)
        self.tempActor.setScale(0.1)
        self.tempActor.loop("walk")





game = Game()
game.run()
