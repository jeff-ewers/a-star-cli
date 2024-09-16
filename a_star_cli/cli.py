import argparse
import random
from a_star import a_star

def generate_random_grid(size, obstacle_probability=0.3):
    #create size x size grid with randomized obstacles
    return [[1 if random.random() < obstacle_probability else 0 for _ in range(size)] for _ in range(size)]

def print_grid(grid, path=None):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            #display path
            if path and (i,j) in path:
                print('*', end=" ")
            #display obstacles
            elif cell == 1:
                print("█", end=" ")
            #display traversable nodes
            else:
                print(".", end=" ")
        print()