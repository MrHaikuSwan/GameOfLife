import numpy as np
#import curses #however this works
import sys
import os
import time

import utils

def random_state(height, width, chance_of_living = 0.5):
    if height is None or width is None:
        height, width = 60, 60
    randfloat = np.random.rand(height, width)
    board_state = np.zeros((height,width), dtype=int)
    for y in range(len(randfloat)):
        for x in range(len(randfloat[y])):
            if randfloat[y,x] > (1 - chance_of_living):
                board_state[y,x] = 1
    return board_state

def load_board_state(fname, height, width):
    with open(fname, 'r') as f:
        array_like = [i.strip() for i in f.readlines()]
        array_like = [list(i) for i in array_like]
        loadfile_state = np.array(array_like, dtype = int)
    loadheight = loadfile_state.shape[0]
    loadwidth = loadfile_state.shape[1]
    if height is None and width is None:
        height, width = loadheight, loadwidth
    board_state = np.zeros((height, width), dtype = int)
    board_state[0:loadheight, 0:loadwidth] = loadfile_state
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
        for x in range(len(state[y])):
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
    outputstrs = []
    outputstrs.append('-'*(width + 2))
    for h in range(height):
        outputstrs.append('|' + utils.row_to_str(state[h]) + '|')
    outputstrs.append('-'*(width + 2))
    outputstr = '\n'.join(outputstrs)
    print outputstr


args = sys.argv[1:]
if not args:
    board_state = random_state(60,60)
else:
    if os.path.isfile(args[0]) and args[0].endswith('.txt'):
        fp = args[0]
        args = args[1:]
    else:
        fp = ''
    board_dims = [int(i) for i in args[:3]]
    if len(board_dims) == 3:
        height = board_dims[0]
        width = board_dims[1]
        chance_of_living = board_dims[2]
    elif len(board_dims) == 2:
        height = board_dims[0]
        width = board_dims[1]
        chance_of_living = 0.5
    elif len(board_dims) == 1:
        height = board_dims[0]
        width = board_dims[0]
        chance_of_living = 0.5
    else:
        height = None
        width = None
        chance_of_living = 0.5
    if fp:
        board_state = load_board_state(fp, height, width)
    else:
        board_state = random_state(height, width, chance_of_living)

while True:
    beg_loop = time.time()
    render(board_state)
    board_state = next_board_state(board_state)
    time.sleep(utils.positive(0.02 - time.time() + beg_loop))
    