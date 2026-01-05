# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from code_from_previous_branches import gol_basic_simulation
from GameBoard import GameBoard
from pathlib import Path
import yaml

def parse_file_name(file_name):
    script_location = Path(__file__).parent
    return script_location / 'test_file.yml'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    total_turns = int(input("Enter number of turns: "))
    game_board = GameBoard()
    print("starting board position:")
    game_board.create_board_from_yaml(parse_file_name("test_file.yml"))

    game_board.print_game_board()
    for current_turn in range(1, total_turns + 1):
        print("current turn: " + str(current_turn))
        game_board.update_game_board()
        game_board.print_game_board()
        game_board.print_counter_of_all_entities()
