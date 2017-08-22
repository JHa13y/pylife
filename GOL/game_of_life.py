import numpy as np
from numpy import genfromtxt
import time
from matplotlib import pyplot as plt
im=None
##Normal Toroid
def main():
    seed = genfromtxt('seed.csv', delimiter=',')
    size = seed.shape[0]
    window = 1;

    current = seed
    while True:
        next = np.zeros(shape=(size, size))
        print_board(current)
        for j in range(0,size):
            for i in range(0,size):
                ##Toroid case
                count =0;

                count += current[(i-1)%size][(j-1)%size]
                count += current[(i - 1) % size][(j + 1) % size]
                count += current[(i + 1) % size][(j - 1) % size]
                count += current[(i + 1) % size][(j + 1) % size]
                count += current[i][(j - 1) % size]
                count += current[i][(j + 1) % size]
                count += current[(i + 1) % size][j]
                count += current[(i - 1) % size][j]

                next[i][j] = evaluate_rules(count, current[i][j])

        current = next
        #time.sleep(0.01)

def evaluate_rules(count, alive):
    """Returns if the cell is alive or dead based upon its current state and neighbor count"""
    if alive == 1:
        if count >= 2 and count <= 3:
            return 1
    elif alive == 0 and count == 3:
        return 1

    return 0

def print_board(board):
    global im
    #print(board)
    #plt.axis([0, 10, 0, 1])
    plt.ion()
    if im is None:
        im = plt.imshow(board, interpolation='nearest')
    im.set_data(board)
    plt.pause(0.005)


if __name__ == "__main__":
        main();