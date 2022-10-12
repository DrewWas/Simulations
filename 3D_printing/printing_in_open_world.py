from direct.showbase.ShowBase import ShowBase
from panda3d.core import *

base = ShowBase()
base.disableMouse()
#base.useDrive()

plane1 = Plane((0, 0, 1), (0, 0, 5))
plane1_np = render.attachNewNode(PlaneNode("plane1", plane1))
plane1_np.show()




base.cam.setPos(0, -150, 0)
base.camera.setP(-30)
base.run()
