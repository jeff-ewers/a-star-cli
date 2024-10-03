
# A* Pathfinding Algorithm CLI

## Overview

This project implements the [A* (A-star) pathfinding algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) with a command-line interface. It generates a random grid with obstacles and finds the shortest path between two points using the A* algorithm. The application visualizes the grid and the found path in the console.

## Features

- Implementation of the A* pathfinding algorithm
- Random grid generation with customizable size and obstacle density
- Command-line interface for easy interaction
- Visualization of the grid and path in the console
- Customizable start and goal positions

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/astar-pathfinding-cli.git
   cd astar-pathfinding-cli
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the CLI application with default settings:

```bash
python cli_app.py
```

### Command-line Arguments

- `--size`: Set the size of the grid (default is 10)
- `--start`: Set the start position (default is 0 0)
- `--goal`: Set the goal position (default is the bottom-right corner)

Example with custom settings:

```bash
python cli_app.py --size 20 --start 5 5 --goal 15 15
```

## Output

The application will display:
1. The initial grid with obstacles
2. The path found by the A* algorithm (if one exists)
3. The grid with the path marked

. represents an open cell
█ represents an obstacle
* represents the path found by the A* algorithm

Example output:

```
Initial grid:
. █ . . █ . . █ . █ █ . . . █ . . █ . .
. . . █ . . █ . . . . █ . █ . . █ . █ .
█ . █ . . █ . . █ . . . █ . . █ . . . █
. . . █ . . . █ . █ █ . . . █ . █ . . .
█ █ . . █ . . . █ . . . █ . . █ . . █ .
. . █ . . █ . . . █ . . . █ . . . █ . █
. █ . . █ . █ █ . . █ . . . █ . █ . . .
█ . . █ . . . . █ . . █ . . . █ . . █ .
. . █ . . █ . . . █ . . . █ . . █ . . █
. █ . . █ . . █ . . █ █ . . . █ . . █ .
█ . . █ . █ . . █ . . . . █ . . █ . . .
. █ . . . . █ . . █ . █ █ . . █ . . █ .
. . █ . █ . . █ . . █ . . . █ . █ . . █
█ . . █ . . █ . . █ . . █ . . . . █ . .
. . █ . . █ . . █ . █ . . . █ . . . █ .
. █ . . █ . █ . . . . █ . . . █ . █ . .
█ . . █ . . . █ . █ . . . █ . . █ . . █
. █ . . . █ . . █ . . █ . . █ . . . █ .
. . █ . . . █ . . . █ . █ . . . █ . . .
█ . . . █ . . . █ . . . . █ . . . █ . .

Finding path from (0, 0) to (19, 19)...

Path found!
* █ . . █ . . █ . █ █ . . . █ . . █ . .
* . . █ . . █ . . . . █ . █ . . █ . █ .
█ * █ . . █ . . █ . . . █ . . █ . . . █
. * . █ . . . █ . █ █ . . . █ . █ . . .
█ █ * . █ . . . █ . . . █ . . █ . . █ .
. . █ * . █ . . . █ . . . █ . . . █ . █
. █ . * █ . █ █ . . █ . . . █ . █ . . .
█ . . █ * . . . █ . . █ . . . █ . . █ .
. . █ . * █ . . . █ . . . █ . . █ . . █
. █ . . █ * . █ . . █ █ . . . █ . . █ .
█ . . █ . █ * . █ . . . . █ . . █ . . .
. █ . . . . █ * . █ . █ █ . . █ . . █ .
. . █ . █ . . █ * . █ . . . █ . █ . . █
█ . . █ . . █ . * █ . . █ . . . . █ . .
. . █ . . █ . . █ * █ . . . █ . . . █ .
. █ . . █ . █ . . * . █ . . . █ . █ . .
█ . . █ . . . █ . █ * . . █ . . █ . . █
. █ . . . █ . . █ . . * . . █ . . . █ .
. . █ . . . █ . . . █ . * . . . █ . . .
█ . . . █ . . . █ . . . . * * * * * *

Path: [(0, 0), (1, 0), (1, 1), (2, 2), (3, 1), (4, 2), (5, 3), (4, 4), (5, 5), (6, 4), (7, 5), (8, 6), (9, 5), (10, 6), (11, 7), (12, 8), (13, 9), (14, 8), (15, 9), (16, 10), (17, 11), (18, 12), (19, 13), (19, 14), (19, 15), (19, 16), (19, 17), (19, 18), (19, 19)]
```

## How It Works

This program implements the A* (A-star) pathfinding algorithm to find the shortest path between two points on a grid. Here's a detailed breakdown:

### 1. Grid Generation

- The program starts by creating a 2D grid of a specified size (default is 10x10).
- Each cell in the grid is either open (.) or an obstacle (█).
- Obstacles are randomly placed based on a probability (default is 30% chance for each cell).

### 2. A* Algorithm Implementation

The A* algorithm uses a best-first search approach to find the optimal path. Here's how it works:

a) **Node Representation:**
   - Each cell on the grid is represented as a Node.
   - Each Node stores:
     * Its position (x, y coordinates)
     * g-score: the cost to reach this node from the start
     * h-score: the estimated cost from this node to the goal (heuristic)
     * f-score: the sum of g-score and h-score
     * A reference to its parent node

b) **Main Algorithm Loop:**
   - Start with the initial node and add it to an 'open list' (a priority queue).
   - While the open list is not empty:
     1. Pop the node with the lowest f-score from the open list.
     2. If this node is the goal, reconstruct and return the path.
     3. Add this node to a 'closed list' to avoid revisiting.
     4. For each neighbor of the current node:
        - If it's an obstacle or in the closed list, skip it.
        - Calculate its g-score (cost from start to this neighbor).
        - If this neighbor is not in the open list or has a better g-score:
          * Update its scores and parent.
          * Add it to the open list if it's not already there.

c) **Heuristic Function:**
   - We use the Euclidean distance as our heuristic.
   - This estimates the straight-line distance between any node and the goal.
   - Formula: sqrt((x2-x1)^2 + (y2-y1)^2)

d) **Path Reconstruction:**
   - Once the goal is reached, we reconstruct the path by following parent links from the goal back to the start.
   - This path is then reversed to give the route from start to goal.

### 3. Visualization

- The program displays the initial grid with obstacles.
- After finding the path, it shows the grid again with the path marked.
- The path is represented by asterisks (*) on the grid.

### 4. Optimizations and Considerations

- The open list is implemented as a heap queue for efficient retrieval of the node with the lowest f-score.
- The closed list is a set for fast lookup to check if a node has been visited.
- The algorithm considers both orthogonal (up, down, left, right) and diagonal movements.
- Diagonal movements have a slightly higher cost (√2 ≈ 1.414) compared to orthogonal movements (1).

### 5. Edge Cases

- If no path is found (e.g., the goal is surrounded by obstacles), the program reports that no path exists.
- If the start or goal positions are obstacles, the program handles this gracefully and reports the issue.

This implementation balances efficiency and accuracy, making it suitable for pathfinding in grid-based environments like games, robotics simulations, or route planning scenarios.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by various pathfinding algorithm implementations and educational resources on A* search.
