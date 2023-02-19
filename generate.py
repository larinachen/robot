import pyrosim.pyrosim as pyrosim

# start pyrosim world and store in box.sdf
pyrosim.Start_SDF("box.sdf")

# add box
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])

# end the world
pyrosim.End()