import pybullet as p
import time

# create physics object
physicsClient = p.connect(p.GUI)
# pybullet.configureDebugVisualizer(pybullet.COV_ENABLE_GUI,0)

# load world from box.sdf
p.loadSDF("box.sdf")

# stepping throuhgh the world using 1000 steps
for i in range(1000):
	print(f"starting iteration {i}")
	p.stepSimulation()
	time.sleep(0.01)


p.disconnect()