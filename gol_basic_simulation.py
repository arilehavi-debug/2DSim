import numpy as np

# receive a configuration text file as a .txt file
# return a numpy array that holds the configuration content
def load_starting_configuration(txt_file_name):
    # catch exception
    try:
        with open(txt_file_name, 'r') as f:
            file_contents = f.read()  # Read the entire file into a single string


    except FileNotFoundError:
        print(f"Error: The file " + txt_file_name + " was not found.")