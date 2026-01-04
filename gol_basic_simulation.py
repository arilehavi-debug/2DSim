"""
this module is in charge of the logic of running the basic gol program
"""
import numpy as np
from numpy.f2py.auxfuncs import throw_error

# CONSTS SEGMENT
VALID_FILE_CHARACTERS = (".", "o")
LIVE_CELL_SYMBOL = "o"
DEAD_CELL_SYMBOL = "."
FILE_NOT_FOUND_MESSAGE = "File not found."

def check_correct_format_file(file_contents: str)-> None:
    """checking if the file contains only valid characters - "." and "0" 

        Args:
            file_contents: content of file received as a string. 

        Returns:
           nothing.

        """
    for char in file_contents:
        if not char in VALID_FILE_CHARACTERS:
            throw_error("invalid characters in file")

def load_starting_configuration(txt_file_name: str) -> np.array:
    """receive a configuration text file as a .txt file
    return a numpy array that holds the configuration content

        Args:
            txt_file_name: file name in the wanted directory

        Returns:
           numpy array representing the table

        """
    try:
        with open(txt_file_name, 'r', encoding='utf-8') as f:
            file_contents = f.read()  # Read the entire file into a single string
            np_table = [[]]
            check_correct_format_file(file_contents)
            for char in file_contents:
                if char == '\n':
                    np_table.append([])
                else:
                    np_table[-1].append(char)
            return np.array(np_table)

    except FileNotFoundError:
        print(FILE_NOT_FOUND_MESSAGE)

    return np_table


def print_simulation(current_state: np.array, current_iteration: int) -> None:
    """function to print the current iteration of the gol

        Args:
            current_state: numpy array representing gol
            current_iteration: current iteration of the game

        Returns:
           None

        """
    print("current iteration: ", current_iteration)
    for row in current_state:
        print(*row)

def determine_cell_state(live_cnt: int, current_value: int) -> chr:
    """function to return relevant character for one cell in accordance to
        the number of live cells adjacent to it

        Args:
            live_cnt: number of live cells next to the current cell
            current_value: current value of cell

        Returns:
           new value of the cell

        """
    if live_cnt == 3:
        return LIVE_CELL_SYMBOL
    if live_cnt == 2:
        return current_value
    return DEAD_CELL_SYMBOL

def check_validity_of_coordiantes(row: int, col: int, row_add: int, col_add: int) -> bool:
    """function that checks if the coordinates are valid
        coordinates in the game table to check neighbouring cells

        Args:
            row: current row to check
            col: current column to check
            row_add: current parameter to add to the row
            col_add: current parameter to add to the column

        Returns:
           True if the coordinates are valid to check
           False otherwise

        """
    if row_add != 0 or col_add != 0:
        if (row + row_add) >= 0 and (col + col_add >= 0):
            return True
    return False

def helper_current_cell(current_iteration: np.array, row: int, col: int) -> chr:
    """used for determining the value of a cell in the next iteration of the program

        Args:
            current_iteration: numpy array representing the current state of the game
            row: row of relevant cell
            col: column of relevant cell

        Returns:
           needed value of the cell in the next iteration

        """
    live_cnt = 0
    row_add = -1

    while row_add != 2:
        for col_add in range(-1, 2):
            try:
                if check_validity_of_coordiantes(row, col, row_add, col_add):
                    if current_iteration[row +row_add][col + col_add] == LIVE_CELL_SYMBOL:
                        live_cnt += 1
            except IndexError:
                pass
        row_add += 1

    return determine_cell_state(live_cnt, current_iteration[row][col])

def update_iteration(current_iteration: int) -> np.array:
    """returns the game board in the next iteration based on the current one

        Args:
            current_iteration: numpy array representing the current state of the game

        Returns:
           game board in the next iteration based on the current one
        """
    next_iteration = [[]]
    for row in range(len(current_iteration)):
        for col in range(len(current_iteration[0])):
            next_iteration[-1].append(helper_current_cell(current_iteration, row, col))

        next_iteration.append([])
    return np.array(next_iteration[:-1])
