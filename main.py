from pathlib import Path

from game_board import GameBoard
from objects.entity import Entity
from event_handling import EventManager, ConsoleObserver


def init_event_manger() -> EventManager:
    """
    Initiating a manager to handle all events in game
    Return:
         event manager to handle all events in game
    """
    mngr = EventManager()
    mngr.subscribe(ConsoleObserver())
    return mngr


def parse_file_name(file_name:str = 'test_file.yml') -> str:
    """
    Returns the path to the yaml file needed to parse
        Args:
            file_name: name of the yaml file to parse
        Return:
           path to yaml file needed to parse as string
    """
    script_location = Path(__file__).parent
    return f"{script_location}/{file_name}"

def run_game_iterations(game_board: list[list[Entity]], total_turns: int) -> None:
    """
    Function to run entire game turns as wanted
    Args:
        game_board: initial game board
        total_turns:  total turns the game would run in
    """
    for current_turn in range(1, total_turns + 1):
        print("current turn: " + str(current_turn))
        game_board.update_game_board(game_manager)
        game_board.print_game_board()
        game_board.print_counter_of_all_entities()


if __name__ == '__main__':
    total_turns = int(input("Enter number of turns: "))
    game_board = GameBoard()
    game_manager = init_event_manger()
    print("starting board position:")
    game_board.create_board_from_yaml(parse_file_name())
    game_board.print_game_board()
    run_game_iterations(game_board, total_turns)
