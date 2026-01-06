"""
main module to run the entire path
"""
from pathlib import Path
from game_board import GameBoard


def parse_file_name() -> str:
    """returns the path to the yaml file needed to parse
            Returns:
               path to string needed to parse
            """
    script_location = Path(__file__).parent
    return script_location / 'test_file.yml'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    total_turns = int(input("Enter number of turns: "))
    game_board = GameBoard()
    print("starting board position:")
    game_board.create_board_from_yaml(parse_file_name())
    game_board.print_game_board()
    for current_turn in range(1, total_turns + 1):
        print("current turn: " + str(current_turn))
        game_board.update_game_board()
        game_board.print_game_board()
        game_board.print_counter_of_all_entities()
