import numpy as np
import os
from numpy.f2py.auxfuncs import throw_error
import time


# receive numpy array of contents
# check validity of file
def check_correct_format_file(file_contents: str):
    for char in file_contents:
        if not(char == "." or char == "o"):
            throw_error("invalid characters in file")

# receive a configuration text file as a .txt file
# return a numpy array that holds the configuration content

def load_starting_configuration(txt_file_name):
    # catch exception in case file name isn't valid
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
def print_simulation(current_state, current_iteration):
    print("current iteration: ", current_iteration)
    #print every row for itself
    for row in current_state:
        print(*row)


# determine wether the current cell should be dead or alive in the next iteration
def determine_cell_state(live_cnt, current_value):
    if live_cnt == 3:
        return "o"
    if live_cnt == 2:
        return current_value
    return "."

# helper function to update te state of a current cell in the simulation
def helper_current_cell(current_iteration, row, col):
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
def update_iteration(current_iteration):
    next_iteration = [[]]
    for row in range(len(current_iteration)):
        for col in range(len(current_iteration[0])):
            next_iteration[-1].append(helper_current_cell(current_iteration, row, col))
        next_iteration.append([])
    return np.array(next_iteration[:-1])






