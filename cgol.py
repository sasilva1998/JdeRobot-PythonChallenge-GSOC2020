# Needed libraries, in this 
# case matplotlib is only used
# for illustration purposes
import json
import argparse
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 
import numpy as np


def addGlider(i, j, grid): 
    glider = np.array([[0,    0, 255],  
                       [255,  0, 255],  
                       [0,  255, 255]]) 
    grid[i:i+3, j:j+3] = glider 
  
def addGosperGliderGun(i, j, grid): 

    gun = np.zeros(11*38).reshape(11, 38) 
    gun[5][1] = gun[5][2] = 255
    gun[6][1] = gun[6][2] = 255
    gun[3][13] = gun[3][14] = 255
    gun[4][12] = gun[4][16] = 255
    gun[5][11] = gun[5][17] = 255
    gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = 255
    gun[7][11] = gun[7][17] = 255
    gun[8][12] = gun[8][16] = 255
    gun[9][13] = gun[9][14] = 255
    gun[1][25] = 255
    gun[2][23] = gun[2][25] = 255
    gun[3][21] = gun[3][22] = 255
    gun[4][21] = gun[4][22] = 255
    gun[5][21] = gun[5][22] = 255
    gun[6][23] = gun[6][25] = 255
    gun[7][25] = 255
    gun[3][35] = gun[3][36] = 255
    gun[4][35] = gun[4][36] = 255
  
    grid[i:i+11, j:j+38] = gun

def addPentadecathlon(i, j, grid):
    penta = np.zeros(10*3).reshape(3,10)

    penta[0][2] = penta[0][7] = 255
    penta[1][0:2] = penta[1][3:7] = penta[1][8] = penta[1][9] = 255
    penta[2][2] = penta[2][7] = 255

    grid[i:i+3, j:j+10] = penta

def addBlinker(i, j, grid):
    blinker = np.zeros(3*3).reshape(3,3)

    blinker[0][1] = blinker[1][1] = blinker[2][1] = 255

    grid[i:i+3, j:j+3] = blinker  


def update(frameNum, img, grid, N): 
  
    # copy grid since we require 8 neighbors  
    # for calculation and we go line by line  
    newGrid = grid.copy() 
    for i in range(N): 
        for j in range(N): 
  
            # compute 8-neghbor sum 
            # using toroidal boundary conditions - x and y wrap around  
            # so that the simulaton takes place on a toroidal surface. 
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255) 
  
            # apply Conway's rules 
            if grid[i, j]  == 255: 
                if (total < 2) or (total > 3): 
                    newGrid[i, j] = 0
            else: 
                if total == 3: 
                    newGrid[i, j] = 255
  
    # update data 
    img.set_data(newGrid) 
    grid[:] = newGrid[:] 
    return img 

def loadConfig(address):

    # opening json file
    with open(address) as f:
        data = json.load(f)

    # retrieving parameters
    N=data['gridsize']
    updateinterval= int(data['interval'])
    return (N,updateinterval)

def gridInit(N):
    grid = np.zeros(N*N).reshape(N, N)

    amount=int(input('Enter amount of patterns to include: '))
    for i in range(0,amount):
        patterntype=int(input("Enter the number according to the pattern:\n0 - Glider\n1 - Gosper Glider Gun\n2 - Pentadecathlon\n3 - Blinker\n"))
        xpos=int(input("Enter X coordinate: "))
        ypos=int(input("Enter Y coordinate: "))

        if patterntype == 0:
            addGlider(xpos,ypos,grid)
        elif patterntype == 1:
            addGosperGliderGun(xpos,ypos,grid)
        elif patterntype == 2:
            addPentadecathlon(xpos,ypos,grid)
        elif patterntype == 3:
            addBlinker(xpos,ypos,grid)      

    return grid

def gameLaunch(grid,N,updateinterval):
    fig, ax = plt.subplots() 
    img = ax.imshow(grid, interpolation='nearest') 
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                              frames = 10, 
                                interval=updateinterval, 
                                save_count=50)
    plt.show()


