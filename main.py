# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from code_from_previous_branches import gol_basic_simulation
from GameBoard import GameBoard
import yaml
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    total_turns = 10
    game_board = GameBoard()
    print("starting board position:")
    game_board.print_game_board()
    for current_turn in range(1, total_turns):
        print("current turn: " + str(current_turn))
        game_board.update_game_board()
        game_board.print_game_board()
        game_board.print_counter_of_all_entities()
