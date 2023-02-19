import pybullet as p
import pybullet_data
import time

# create physics object
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# pybullet.configureDebugVisualizer(pybullet.COV_ENABLE_GUI,0)

# load world from box.sdf
# set world parameters
p.setGravity(0,0,-9.8)
# add floor
planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")

# stepping throuhgh the world using 1000 steps
for i in range(1000):
	print(f"starting iteration {i}")
	p.stepSimulation()
	time.sleep(0.01)


p.disconnect()