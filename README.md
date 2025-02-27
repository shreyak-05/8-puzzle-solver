
# 8-Puzzle Solver

This Python script solves the 8-puzzle problem using Breadth-First Search (BFS).

## Requirements
1. Install Python 3.x from python.org.
2. Install the required libraries
 ```bash
    pip install numpy pygame


1.  Save the Python script as a `.py` file (e.g., `8puzzle.py`).
2.  Run the script from the command line: `python 8puzzle.py`
3.  The script will generate three output files: `Nodes.txt`, `NodesInfo.txt`, and `nodePath.txt`.

## Input

-   The initial state of the puzzle is defined within the `initial_puzzle_state` variable in the script.
-   The goal state is defined within the `goal_state` variable in the script.

## Output

-   `Nodes.txt`: Contains all the explored states.
-   `NodesInfo.txt`: Contains information about each explored node (index, parent index, state).
-   `nodePath.txt`: Contains the solution path from the initial state to the goal state.

## Animate

- Run the Animate.py script to animate the solution:
 ```bash
    python Animate.py

## Algorithm

-   Breadth-First Search (BFS) is used to explore the state space.
-   Backtracking is used to reconstruct the solution path.

## Notes

-   The script can find solutions for puzzles that require up to 31 steps.
-   The script is designed to run within a reasonable time frame (under   /10 minutes).
