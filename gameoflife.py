import numpy as np
import time

import utils

def random_state(height, width):
    board_state = np.random.randint(2, size = (height, width))
    return board_state

def get_neighbors(state,x,y):
    state = np.copy(state)
    max_y, max_x = state.shape
    xs = [x + n for n in [-1,0,1] if x + n in range(max_x)]
    ys = [y + n for n in [-1,0,1] if y + n in range(max_y)]
    neighbors = []
    for y_coord in ys:
        for x_coord in xs:
            if (x_coord, y_coord) != (x,y):    
                neighbors.append(state[y_coord, x_coord])
    return neighbors

def next_board_state(state):
    state = np.copy(state)
    new_state = np.zeros(state.shape, dtype=int)
    for y in range(len(state)):
        for x in range(len(state)):
            neighbors = get_neighbors(state,x,y)
            living_neighbors = len([i for i in neighbors if i == 1])
            if state[y,x] == 1:
                if living_neighbors in (0,1):
                    new_state[y,x] = 0
                elif living_neighbors in (2,3):
                    new_state[y,x] = 1
                else:
                    new_state[y,x] = 0
            else:
                if living_neighbors == 3:
                    new_state[y,x] = 1
    return new_state

def render(state):
    height, width = state.shape
    print '-'*(width + 2)
    for h in range(height):
        print '|' + utils.row_to_str(state[h]) + '|'
    print '-'*(width + 2)
    
    
board_state = random_state(50,50)

while True:
    render(board_state)
    board_state = next_board_state(board_state)
    time.sleep(0.25)