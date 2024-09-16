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

def main():
    parser = argparse.ArgumentParser(description="A* Pathfinding Algorithm Demo")
    parser.add_argument("--size", type=int, default=10, help="Size of the grid")
    parser.add_argument("--start", type=int, nargs=2, default=[0,0], help="Start position (row column)")
    parser.add_argument("--goal", type=int, nargs=2, default=None, help="Goal position (row column)")
    args = parser.parse_args()

    grid = generate_random_grid(args.size)
    start = tuple(args.start)
    goal = tuple(args.goal) if args.goal else (args.size - 1, args.size - 1)

    print("Initial grid:")
    print_grid(grid)

    print(f"Finding path from {start} to {goal}...")

    #find path using A*
    path = a_star(grid, start, goal)

    if path:
        print("\nPath found!")
        print_grid(grid, path)
        print(f"\nPath: {path}")
    else:
        print("\nNo path found.")

if __name__ == "__main__":
    main()
