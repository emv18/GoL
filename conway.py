"""

Eduardo Morales Vizcarra and Gabriel Castillo
id 0226265

conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from datetime import date
import os
import time

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, ON], 
                       [ON,  0, ON], 
                       [0,  ON, ON]])
    grid[i:i+3, j:j+3] = glider

def vecinos(bord,cell, i) -> int:
    NB = bord[cell[0],cell[1]] + bord[cell[0],cell[1] +1] + bord[cell[0],cell[1]-1]
    NB += bord[cell[0]+1,cell[1]] + bord[cell[0]+1,cell[1] +1] + bord[cell[0]+1,cell[1]-1]
    NB += bord[cell[0]-1,cell[1]] + bord[cell[0]-1,cell[1] +1] + bord[cell[0]-1 ,cell[1]-1]
    NB /= ON
    return NB

def iteracion(itera, iter):
    itera.append(iter)
    return itera

def update(frameNum, img, grid, N, width, height, generation, itera, aGeneration):
    
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    iterac= iteracion(itera, aGeneration)
    iteraciones= len(iterac)
    countBlock= 0
    countBee= 0
    countLoaf= 0
    countBoat= 0
    countTub= 0
    countBlinker= 0
    countToad= 0
    countBeacon= 0
    countGlider= 0
    countLws= 0
    time.sleep(0.5)
    # TODO: Implement the rules of Conway's Game of Life
    if (iteraciones < generation):
        newGrid = grid.copy()
        for i in range(width):
            for j in range(height):
                NB = vecinos(grid,(i,j), j)
                if(grid[i,j] == ON):
                    NB-= 1
                if(grid[i,j] == OFF):
                    if(NB == 3):
                        newGrid[i,j]=ON
                elif(grid[i,j]==ON):
                    if (NB < 2 or NB > 3):
                            newGrid[i, j] = OFF
    # update data
        grid[:] = newGrid[:]
        img.set_data(grid)

        block = np.array([[0, 0, 0, 0],
                          [0, ON, ON, 0], 
                          [0, ON, ON, 0], 
                          [0, 0, 0, 0]])
        
        beehive = np.array([[0, 0, 0, 0, 0, 0],
                            [0, 0, ON, ON, 0, 0],
                            [0, ON, 0, 0, ON, 0],
                            [0, 0, ON, ON, 0, 0],
                            [0, 0, 0, 0, 0, 0]])
        
        loaf = np.array([[0, 0, 0, 0, 0, 0],
                         [0, 0, ON, ON, 0, 0],
                         [0, ON, 0, 0, ON, 0],
                         [0, 0, ON, 0, ON, 0],
                         [0, 0,   0, ON,   0, 0],
                         [0, 0, 0, 0, 0, 0]])

        boat = np.array([[0, 0, 0, 0, 0],
                         [0, ON, ON, 0, 0], 
                         [0, ON, 0, ON, 0], 
                         [0, 0, ON, 0, 0],
                         [0, 0, 0, 0, 0]])
        
        tub = np.array([[0, 0, 0, 0, 0],
                        [0, 0, ON, 0, 0], 
                        [0, ON, 0, ON, 0], 
                        [0, 0, ON, 0, 0],
                        [0, 0, 0, 0, 0]])
    
        blinker1 = np.array([[0, 0, 0],
                             [0, ON, 0], 
                             [0, ON, 0], 
                             [0, ON, 0],
                             [0, 0, 0]])
        
        blinker2 = np.array([[0, 0, 0, 0, 0],
                             [0, ON, ON, ON, 0],
                             [0, 0, 0, 0, 0]])
        
        toad1 = np.array([[0, 0, 0, 0, 0, 0],
                          [0, 0, 0, ON, 0, 0],
                          [0, ON, 0, 0, ON, 0],
                          [0, ON, 0, 0, ON, 0],
                          [0, 0, ON, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0]])
        
        toad2 = np.array([[0, 0, 0, 0, 0, 0],
                          [0, 0, ON, ON, ON, 0],
                          [0, ON, ON, ON, 0, 0],
                          [0, 0, 0, 0, 0, 0]])
        
        beacon1 = np.array([[0, 0, 0, 0, 0, 0],
                            [0, ON, ON, 0, 0, 0],
                            [0, ON, ON, 0, 0, 0],
                            [0, 0, 0, ON, ON, 0],
                            [0, 0, 0, ON, ON, 0],
                            [0, 0, 0, 0, 0, 0]])
        
        beacon2 = np.array([[0, 0, 0, 0, 0, 0],
                            [0, ON, ON, 0, 0, 0],
                            [0, ON, 0, 0, 0, 0],
                            [0, 0, 0, 0, ON, 0],
                            [0, 0, 0, ON, ON, 0],
                            [0, 0, 0, 0, 0, 0]])
        
        glider1 = np.array([[0, 0, 0, 0, 0],
                            [0, 0, ON, 0, 0], 
                            [0, 0, 0, ON, 0], 
                            [0, ON, ON, ON, 0],
                            [0, 0, 0, 0, 0]])
        
        glider2 = np.array([[0, 0, 0, 0, 0],
                            [0, ON, 0, ON, 0], 
                            [0, 0, ON, ON, 0], 
                            [0, 0, ON, 0, 0],
                            [0, 0, 0, 0, 0]])
        
        glider3 = np.array([[0, 0, 0, 0, 0],
                            [0, 0, 0, ON, 0], 
                            [0, ON, 0, ON, 0], 
                            [0, 0, ON, ON, 0],
                            [0, 0, 0, 0, 0]])
        
        glider4 = np.array([[0, 0, 0, 0, 0],
                            [0, ON, 0, 0, 0], 
                            [0, 0, ON, ON, 0], 
                            [0, ON, ON, 0, 0],
                            [0, 0, 0, 0, 0]])
    
        lws1 = np.array([[0, 0, 0, 0, 0, 0, 0],
                         [0, ON, 0, 0, ON, 0, 0], 
                         [0, 0, 0, 0, 0, ON, 0], 
                         [0, ON, 0, 0, 0, ON, 0],
                         [0, 0, ON, ON, ON, ON, 0],
                         [0, 0, 0, 0, 0, 0, 0]])
        
        lws2 = np.array([[0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, ON, ON, 0, 0], 
                         [0, ON, ON, 0, ON, ON, 0], 
                         [0, ON, ON, ON, ON, 0, 0],
                         [0, 0, ON, ON, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0]])
        
        lws3 = np.array([[0, 0, 0, 0, 0, 0, 0],
                         [0, 0, ON, ON, ON, ON, 0], 
                         [0, ON, 0, 0, 0, ON, 0], 
                         [0, 0, 0, 0, 0, ON, 0],
                         [0, ON, 0, 0, ON, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0]])
        
        lws4 = np.array([[0, 0, 0, 0, 0, 0, 0],
                         [0, 0, ON, ON, 0, 0, 0], 
                         [0, ON, ON, ON, ON, 0, 0], 
                         [0, ON, ON, 0, ON, ON, 0],
                         [0, 0, 0, ON, ON, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0]])
        
        for i in range(0, width):
            for j in range(0, height):
                    if(np.array_equal(grid[i:i+4, j:j+4] , block, equal_nan=True) ):
                        countBlock+=1
                        continue
                    if(np.array_equal(grid[i:i+5, j:j+6] , beehive, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+5] , np.rot90(beehive), equal_nan=True)):
                        countBee+=1
                        continue
                    if(np.array_equal(grid[i:i+6, j:j+6] , loaf, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+6] , np.rot90(loaf), equal_nan=True) or np.array_equal(grid[i:i+6, j:j+6] , np.rot90(loaf, 2), equal_nan=True) or np.array_equal(grid[i:i+6, j:j+6] , np.rot90(loaf, 3), equal_nan=True)):
                        countLoaf+=1
                        continue
                    if(np.array_equal(grid[i:i+5, j:j+5] , boat, equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(boat), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(boat, 2), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(boat, 3), equal_nan=True)):
                        countBoat+=1
                        continue
                    if(np.array_equal(grid[i:i+5, j:j+5] , tub, equal_nan=True)):
                        countTub+=1
                        continue
                    if(np.array_equal(grid[i:i+5, j:j+3] , blinker1, equal_nan=True) or np.array_equal(grid[i:i+3, j:j+5] , blinker2, equal_nan=True)):
                        countBlinker+=1
                        continue
                    if(np.array_equal(grid[i:i+6, j:j+6] , toad1, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+6] , np.rot90(toad1), equal_nan=True)):
                        countToad+=1
                        continue
                    if(np.array_equal(grid[i:i+4, j:j+6] , toad2, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+4] , np.rot90(toad2), equal_nan=True)):
                        countToad+=1
                        continue
                    if(np.array_equal(grid[i:i+6, j:j+6] , beacon1, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+6] , np.rot90(beacon1), equal_nan=True)):
                        countBeacon+=1
                        continue
                    if(np.array_equal(grid[i:i+6, j:j+6] , beacon2, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+6] , np.rot90(beacon2), equal_nan=True)):
                        countBeacon+=1
                        continue
                    if(np.array_equal(grid[i:i+5, j:j+5] , glider1, equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider1), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider1, 2), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider1, 3), equal_nan=True)):
                        countGlider+=1
                        continue
                    if(np.array_equal(grid[i:i+5, j:j+5] , glider2, equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider2), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider2, 2), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider2, 3), equal_nan=True)):
                        countGlider+=1
                        continue
                    if(np.array_equal(grid[i:i+5, j:j+5] , glider3, equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider3), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider3, 2), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider3, 3), equal_nan=True)):
                        countGlider+=1
                        continue
                    if(np.array_equal(grid[i:i+5, j:j+5] , glider4, equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider4), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider4, 2), equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5] , np.rot90(glider4, 3), equal_nan=True)):
                        countGlider+=1
                        continue
                    if(np.array_equal(grid[i:i+6, j:j+7] , lws1, equal_nan=True) or np.array_equal(grid[i:i+7, j:j+6] , np.rot90(lws1), equal_nan=True) or np.array_equal( grid[i:i+6, j:j+7] , np.rot90(lws1, 2), equal_nan=True) or np.array_equal( grid[i:i+7, j:j+6] , np.rot90(lws1, 3), equal_nan=True)):
                        countLws+=1
                        continue
                    if(np.array_equal(grid[i:i+6, j:j+7] , lws2, equal_nan=True) or np.array_equal(grid[i:i+7, j:j+6] , np.rot90(lws2), equal_nan=True) or np.array_equal( grid[i:i+6, j:j+7] , np.rot90(lws2, 2), equal_nan=True) or np.array_equal( grid[i:i+7, j:j+6] , np.rot90(lws2, 3), equal_nan=True)):
                        countLws+=1
                        continue
                    if(np.array_equal(grid[i:i+6, j:j+7] , lws3, equal_nan=True) or np.array_equal(grid[i:i+7, j:j+6] , np.rot90(lws3), equal_nan=True) or np.array_equal( grid[i:i+6, j:j+7] , np.rot90(lws3, 2), equal_nan=True) or np.array_equal( grid[i:i+7, j:j+6] , np.rot90(lws3, 3), equal_nan=True)):
                        countLws+=1
                        continue
                    if(np.array_equal(grid[i:i+6, j:j+7] , lws4, equal_nan=True) or np.array_equal(grid[i:i+7, j:j+6] , np.rot90(lws4), equal_nan=True) or np.array_equal( grid[i:i+6, j:j+7] , np.rot90(lws4, 2), equal_nan=True) or np.array_equal( grid[i:i+7, j:j+6] , np.rot90(lws4, 3), equal_nan=True)):
                        countLws+=1
                        continue

        output_file = 'output.txt'
        File(output_file, countBlock, countBee, countLoaf, countBoat, countTub, countBlinker, countToad, countBeacon, countGlider, countLws, aGeneration, iteraciones,  width, height)
        return img,

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments

    aGeneration= 0
    input_file = '1.in' 
    coord= []
    with open(input_file, 'r') as f:
        lines = f.readlines()
        size= lines[0] 
        size= size.split(' ')
        width= int(size[0])
        height= int(size[1])
        generation= lines[1]
        generation= generation.split(' ')
        generation= int(generation[0])
        lines.remove(lines[0])
        lines.remove(lines[0])
        for i in lines:
            i= i.split(' ')
            x= int(i[0])
            y= int(i[1])
            coord.append((x,y))

        

    # declare grid
    grid = np.array([])
    grid = np.zeros((width+1, height+1), dtype=int)

    for i in coord:
        grid[i]= ON
    
    # set grid size
    N = 3
    
    # set animation update interval
    updateInterval = 1


    # populate grid with random on/off - more off than on
    #grid = randomGrid(N)
    # Uncomment lines to see the "glider" demo
    #grid = np.zeros(width, height).reshape(N, N)
    #addGlider(1, 1, grid)
    itera= []
    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, width, height, generation, itera, aGeneration),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)
    plt.show()

    countBlock= 0
    countBee= 0
    countLoaf= 0
    countBoat= 0
    countTub= 0
    countBlinker= 0
    countToad= 0
    countBeacon= 0
    countGlider= 0
    countLws= 0
    iteraciones= 0
    output_file = 'output.txt'
    if(os.path.exists(output_file)):
        os.remove(output_file)
        File(output_file, countBlock, countBee, countLoaf, countBoat, countTub, countBlinker, countToad, countBeacon, countGlider, countLws, aGeneration, iteraciones,  width, height)
    else:
        File(output_file, countBlock, countBee, countLoaf, countBoat, countTub, countBlinker, countToad, countBeacon, countGlider, countLws, aGeneration, iteraciones,  width, height)


def File(output_file, countBlock, countBee, countLoaf, countBoat, countTub, countBlinker, countToad, countBeacon, countGlider, countLws, aGeneration, iteraciones, width, height):
    today = date.today()
    countTotal= countBlock + countBee + countLoaf + countBoat + countTub + countBlinker + countToad + countBeacon + countGlider + countLws
    percentBlock= 0
    percentBee= 0
    percentLoaf= 0
    percentBoat= 0
    percentTub= 0
    percentBlinker= 0
    percentToad= 0
    percentBeacon=0
    percentGlider= 0
    percentLws= 0
    if(countTotal != 0):
        percentBlock= (countBlock/countTotal)*100
        percentBee= (countBee/countTotal)*100
        percentLoaf= (countLoaf/countTotal)*100
        percentBoat= (countBoat/countTotal)*100
        percentTub= (countTub/countTotal)*100
        percentBlinker= (countBlinker/countTotal)*100
        percentToad= (countToad/countTotal)*100
        percentBeacon= (countBeacon/countTotal)*100
        percentGlider= (countGlider/countTotal)*100
        percentLws= (countLws/countTotal)*100
    iteraciones+= 1

    with open(output_file, 'a') as fo:
        fo.write("Simulation at " + str(today) + '\n')
        fo.write("Universe size " + str(width) + " x " + str(height) + ' \n')
        fo.write("Iteration: " + str(iteraciones) + '\n')
        fo.write("----------------------------------------------" + '\n')
        fo.write("|                  |   Count   |   Percent   |" + '\n')
        fo.write("|--------------------------------------------|" + '\n')
        fo.write("| Block            |     " + str(countBlock) + "     |      " + str(percentBlock) + "%      |" + '\n')
        fo.write("| Beehive          |     " + str(countBee) + "     |      " + str(percentBee) + "%      |" + '\n')
        fo.write("| Loaf             |     " + str(countLoaf) + "     |      " + str(percentLoaf) + "%      |" + '\n')
        fo.write("| Boat             |     " + str(countBoat) + "     |      " + str(percentBoat) + "%      |" + '\n')
        fo.write("| Tub              |     " + str(countTub) + "     |      " + str(percentTub) + "%      |" + '\n')
        fo.write("| Blinker          |     " + str(countBlinker) + "     |      " + str(percentBlinker) + "%      |" + '\n')
        fo.write("| Toad             |     " + str(countToad) + "     |      " + str(percentToad) + "%      |" + '\n')
        fo.write("| Beacon           |     " + str(countBeacon) + "     |      " + str(percentBeacon) + "%      |" + '\n')
        fo.write("| Glider           |     " + str(countGlider) + "     |      " + str(percentGlider) + "%      |" + '\n')
        fo.write("| LG sp ship       |     " + str(countLws) + "     |      " + str(percentLws) + "%      |" + '\n')
        fo.write("|--------------------------------------------|" + '\n')
        fo.write("| Total            |     " + str(countTotal) + "     |             |" + '\n')
        fo.write("           " + '\n')
        fo.close()
# call main
if __name__ == '__main__':
    main()