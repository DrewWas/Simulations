from direct.showbase.ShowBase import ShowBase
from panda3d.core import *

class Game(ShowBase):
    def __init__(self):
        # window set up
        ShowBase.__init__(self)
        properties = WindowProperties()
        properties.setSize(1000,700)
        self.win.requestProperties(properties)


        # create plane


        # camera shit



game = Game()
game.run()
