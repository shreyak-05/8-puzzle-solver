#!/usr/bin/env python
# Importing necessary libraries
import numpy as np  # Importing numpy for matrix operations
from collections import deque  # Importing deque for efficient queue operations

# Function to display the puzzle state in a 3x3 matrix format
def display_puzzle(puzzle_state):
    puzzle_matrix = np.array(puzzle_state).reshape(3, 3)  # Reshape the puzzle state into a 3x3 matrix
    return puzzle_matrix  # Return the matrix

# Function to locate the blank tile (represented by 0) in the puzzle state
def locate_blank_tile(puzzle_state):
    puzzle_matrix = np.reshape(puzzle_state, (3, 3))  # Reshape the puzzle state into a 3x3 matrix
    for row_index in range(3):  # Iterate over each row
        for col_index in range(3):  # Iterate over each column
            if puzzle_matrix[row_index][col_index] == 0:  # Check if the current tile is the blank tile
                return [row_index, col_index]  # Return the position of the blank tile

# Function to perform a left move on the puzzle state
def perform_left_move(puzzle_state):
    row, col = locate_blank_tile(puzzle_state)  # Locate the blank tile
    if col != 0:  # Check if the blank tile is not in the first column
        puzzle_state[row][col-1], puzzle_state[row][col] = puzzle_state[row][col], puzzle_state[row][col-1]  # Swap the blank tile with the tile to its left
        return puzzle_state, True  # Return the updated puzzle state and a flag indicating a valid move
    else:
        return puzzle_state, False  # Return the puzzle state and a flag indicating an invalid move

# Function to perform a right move on the puzzle state
def perform_right_move(puzzle_state):
    row, col = locate_blank_tile(puzzle_state)  # Locate the blank tile
    if col != 2:  # Check if the blank tile is not in the last column
        puzzle_state[row][col+1], puzzle_state[row][col] = puzzle_state[row][col], puzzle_state[row][col+1]  # Swap the blank tile with the tile to its right
        return puzzle_state, True  # Return the updated puzzle state and a flag indicating a valid move
    else:
        return puzzle_state, False  # Return the puzzle state and a flag indicating an invalid move

# Function to perform an up move on the puzzle state
def perform_up_move(puzzle_state):
    row, col = locate_blank_tile(puzzle_state)  # Locate the blank tile
    if row != 0:  # Check if the blank tile is not in the first row
        puzzle_state[row-1][col], puzzle_state[row][col] = puzzle_state[row][col], puzzle_state[row-1][col]  # Swap the blank tile with the tile above it
        return puzzle_state, True  # Return the updated puzzle state and a flag indicating a valid move
    else:
        return puzzle_state, False  # Return the puzzle state and a flag indicating an invalid move

# Function to perform a down move on the puzzle state
def perform_down_move(puzzle_state):
    row, col = locate_blank_tile(puzzle_state)  # Locate the blank tile
    if row != 2:  # Check if the blank tile is not in the last row
        puzzle_state[row+1][col], puzzle_state[row][col] = puzzle_state[row][col], puzzle_state[row+1][col]  # Swap the blank tile with the tile below it
        return puzzle_state, True  # Return the updated puzzle state and a flag indicating a valid move
    else:
        return puzzle_state, False  # Return the puzzle state and a flag indicating an invalid move

# Function to flatten a 3x3 matrix into a list
def flatten_matrix(puzzle_matrix):
    flat_list = []  # Initialize an empty list
    for row in puzzle_matrix.tolist():  # Convert the matrix to a list of lists and iterate over each row
        flat_list.extend(row)  # Extend the flat list with the elements of the current row
    return flat_list  # Return the flattened list

# Function to check if the puzzle is solvable
def check_puzzle_solvability(puzzle_state):
    inversion_counts = []  # Initialize a list to store inversion counts
    for index, tile in enumerate(puzzle_state):  # Iterate over each tile in the puzzle state
        if tile != 0:  # Skip the blank tile
            count = 0  # Initialize the inversion count for the current tile
            sub_state = puzzle_state[index:]  # Get the sub-state starting from the current tile
            for sub_tile in sub_state:  # Iterate over each tile in the sub-state
                if sub_tile < tile and sub_tile != 0:  # Check if the sub-tile is less than the current tile and not the blank tile
                    count += 1  # Increment the inversion count
            inversion_counts.append(count)  # Append the inversion count to the list
    total_inversions = sum(inversion_counts)  # Calculate the total number of inversions
    return total_inversions % 2 == 0  # Return True if the total number of inversions is even, indicating the puzzle is solvable

# Test cases
initial_puzzle = [6, 4, 7, 8, 5, 0, 3, 2, 1]  # Initial puzzle state
target_goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # Target goal state

# 1. data structures used to store the node information such as node state, node index, and parent node index
explored_states = set()  # Initialize a set to store explored states
search_path = []  # Initialize a list to store the search path
search_path.append([initial_puzzle])  # Add the initial puzzle state to the search path
goal_found_flag = False  # Initialize a flag to indicate if the goal has been found

is_solvable_flag = check_puzzle_solvability(initial_puzzle)  # Check if the initial puzzle is solvable

# Function to solve the puzzle using Breadth-First Search (BFS)
def solve_puzzle_bfs(start_state, goal_state):
    global explored_states  # Declare the global variable for explored states
    global is_solvable_flag  # Declare the global variable for solvability flag
    global goal_found_flag  # Declare the global variable for goal found flag

    if start_state == goal_state:  # Check if the start state is already the goal state
        print("Initial puzzle is already the goal state.")  # Print a message indicating no moves are needed
        print("No moves needed.")  # Print a message indicating no moves are needed
        return  # Return from the function

    if not is_solvable_flag:  # Check if the puzzle is unsolvable
        print("This puzzle is unsolvable!")  # Print a message indicating the puzzle is unsolvable
        return  # Return from the function

# 4. The code should be able to find the solution for an input that needs up to 31 steps within 10 minute (use of deque)
    search_queue = deque([start_state])  # Initialize a queue with the start state
    visited_nodes = set()  # Initialize a set to store visited nodes
    visited_nodes.add(tuple(start_state))  # Add the start state to the visited nodes
    parent_nodes = {tuple(start_state): None}  # Initialize a dictionary to store parent nodes

    while search_queue:  # Loop until the search queue is empty
        current_node = search_queue.popleft()  # Dequeue the front node
        if current_node == goal_state:  # Check if the current node is the goal state
            print("Goal state has been reached!")  # Print a message indicating the goal state has been reached
            goal_found_flag = True  # Set the goal found flag to True
            break  # Break the loop

#2. Functions for generating new nodes from the parent nodes and checking for duplicate/visited nodes
        for move_function in [perform_left_move, perform_right_move, perform_up_move, perform_down_move]:  # Iterate over each move function
            next_node, is_valid_move = move_function(display_puzzle(current_node.copy()))  # Perform the move and get the next node and validity flag
            next_node = flatten_matrix(next_node)  # Flatten the next node
            if is_valid_move and tuple(next_node) not in visited_nodes:  # Check if the move is valid and the next node is not visited
                search_queue.append(next_node)  # Enqueue the next node
                visited_nodes.add(tuple(next_node))  # Add the next node to the visited nodes
                parent_nodes[tuple(next_node)] = current_node  # Set the parent of the next node to the current node

#3. Implementation of backtracking to find the correct path
    solution_path = []  # Initialize a list to store the solution path
    current_node = goal_state  # Start from the goal state
    while current_node is not None:  # Loop until the current node is None
        solution_path.append(current_node)  # Append the current node to the solution path
        current_node = parent_nodes.get(tuple(current_node))  # Get the parent of the current node
    solution_path.reverse()  # Reverse the solution path

    print("Solution Path:")  # Print a message indicating the solution path
    for node in solution_path:  # Iterate over each node in the solution path
        print(display_puzzle(node))  # Print the node in matrix format
        print()  # Print a blank line
    print(f"Total moves required: {len(solution_path) - 1}")  # Print the total number of moves required

    with open('nodePath.txt', 'w') as path_file:  # Open the nodePath.txt file in write mode
        for node in solution_path:  # Iterate over each node in the solution path
            matrix = display_puzzle(node)  # Get the matrix representation of the node
            column_wise = ' '.join(str(matrix[i][j]) for j in range(3) for i in range(3))  # Convert the matrix to a column-wise string
            path_file.write(column_wise + '\n')  # Write the column-wise string to the file

    with open('Nodes.txt', 'w') as nodes_file:  # Open the Nodes.txt file in write mode
        for node in visited_nodes:  # Iterate over each visited node
            nodes_file.write(' '.join(map(str, node)) + '\n')  # Write the node to the file

    with open('NodesInfo.txt', 'w') as info_file:  # Open the NodesInfo.txt file in write mode
        for index, node in enumerate(solution_path):  # Iterate over each node in the solution path with its index
            info_file.write(f'{index} \t{index}\n')  # Write the index and index to the file

solve_puzzle_bfs(initial_puzzle, target_goal)  # Call the solve_puzzle_bfs function with the initial puzzle and target goal