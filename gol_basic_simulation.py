import numpy
import numpy as np
from numpy.f2py.auxfuncs import throw_error

def check_correct_format_file(file_contents: str)-> None:
    """checking if the file contains only valid characters - "." and "0" 

        Args:
            file_contents: content of file received as a string. 

        Returns:
           nothing.

        Raises:
            TypeError: If the file contains invalid characters."""
    for char in file_contents:
        if not(char == "." or char == "o"):
            throw_error("invalid characters in file")

# receive a configuration text file as a .txt file
# return a numpy array that holds the configuration content

def load_starting_configuration(txt_file_name: str) -> np.array:
    """receive a configuration text file as a .txt file
    return a numpy array that holds the configuration content

        Args:
            txt_file_name: file name in the wanted directory

        Returns:
           numpy array representing the table

        Raises:
            FileNotFoundError: if the file name isn't valid"""
    try:
        with open(txt_file_name, 'r') as f:
            file_contents = f.read()  # Read the entire file into a single string
            np_table = [[]]
            check_correct_format_file(file_contents)
            # read contents of table and check that it's in the correct format
            for char in file_contents:
                if char == '\n':
                    np_table.append([])
                else:
                    np_table[-1].append(char)
            return np.array(np_table)


    except FileNotFoundError:
        print(f"Error: The file " + txt_file_name + " was not found.")

    return np_table


# prints current state of the simulation
def print_simulation(current_state: numpy.array, current_iteration: int) -> None:
    """function to print the current iteration of the gol

        Args:
            current_state: numpy array representing gol
            current_iteration: current iteration of the game

        Returns:
           None

        Raises:
            None"""
    print("current iteration: ", current_iteration)
    # print every row for itself
    for row in current_state:
        print(*row)


# determine wether the current cell should be dead or alive in the next iteration
def determine_cell_state(live_cnt: int, current_value: int) -> chr:
    """function to return relevant character for one cell in accordance to
        the number of live cells adjacent to it

        Args:
            live_cnt: number of live cells next to the current cell
            current_value: current value of cell

        Returns:
           new value of the cell

        Raises:
            None"""
    if live_cnt == 3:
        return "o"
    if live_cnt == 2:
        return current_value
    return "."

# helper function to update te state of a current cell in the simulation
def helper_current_cell(current_iteration: numpy.array, row: int, col: int) -> chr:
    """used for determining the value of a cell in the next iteration of the program

        Args:
            current_iteration: numpy array representing the current state of the game
            row: row of relevant cell
            col: column of relevant cell

        Returns:
           needed value of the cell in the next iteration

        Raises:
            None"""
    live_cnt = 0 #counter for live cells that are adjacent to the current cell
    row_add = -1

    # continue counter until we end the process of counting neighbours
    while row_add != 2:
            for col_add in range(-1, 2):
                try:
                    if row_add != 0 or col_add != 0: # checking we arent comparing the cell to itself
                        if (row + row_add) >= 0 and (col + col_add >= 0):
                            if current_iteration[row + row_add][col + col_add] == 'o':
                                live_cnt += 1
                except IndexError:
                    pass
            row_add += 1

    return determine_cell_state(live_cnt, current_iteration[row][col])


# update iteration of the game
# returns the next iteration
def update_iteration(current_iteration: int) -> numpy.array:
    """returns the game board in the next iteration based on the current one

        Args:
            current_iteration: numpy array representing the current state of the game

        Returns:
           game board in the next iteration based on the current one

        Raises:
            None"""
    next_iteration = [[]]
    for row in range(len(current_iteration)):
        for col in range(len(current_iteration[0])):
            next_iteration[-1].append(helper_current_cell(current_iteration, row, col))
        next_iteration.append([])
    return np.array(next_iteration[:-1])