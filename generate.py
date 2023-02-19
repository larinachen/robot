import pyrosim.pyrosim as pyrosim

# start pyrosim world and store in box.sdf
pyrosim.Start_SDF("boxes.sdf")

# add box
length, width, height = 1, 1, 1
x, y, z = 0, 0, 0.5
# 3 x 3 grid of towers
for r in range(3):
    x += length
    for c in range(3):
        y += width
        # generate a single tower
        for i in range(10):
            pyrosim.Send_Cube(name="Box1", pos=[x,y,z] , size=[length, width, height])
            z += height
            length, width, height = 0.9*length, 0.9*width, 0.9*height
        z = 0.5
        length, width, height = 1, 1, 1 
    y = 0   
    
    

# end the world
pyrosim.End()