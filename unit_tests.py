from gameoflife import next_board_state
import numpy as np

# TODO: there's a lot of repeated code here. Can
# you move some of into reusable functions to
# make it shorter and neater?

def check_func(func, indata, expectedoutdata):
    funcoutdata = func(indata)
    if np.all(expectedoutdata == funcoutdata):
        print "Passed!"
    else:
        print "Failed! :("
        print "Expected:"
        print expectedoutdata
        print "Actual:"
        print funcoutdata

if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = np.array([
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ])
    expected_next_state1 = np.array([
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ])
    check_func(next_board_state, init_state1, expected_next_state1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = np.array([
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ])
    expected_next_state2 = np.array([
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ])
    actual_next_state2 = next_board_state(init_state2)

    check_func(next_board_state, init_state2, expected_next_state2)