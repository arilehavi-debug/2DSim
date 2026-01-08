from pathlib import Path

from game_board import GameBoard
from objects.entity import Entity
from event_handling.event_manager import EventManager
from lib_consts.main_consts import OBSERVER_TYPES_TO_INIT


def sign_users_to_events(mngr: EventManager):
    """
    Signing all observers in the program
    for the event manager to handle.
    Args:
        mngr: Event manager for the game
    """
    for observer in OBSERVER_TYPES_TO_INIT:
        observer(mngr)


def init_event_manger() -> EventManager:
    """
    Initiating a manager to handle all events in game.
    Return:
         event manager to handle all events in game
    """
    mngr = EventManager()
    return mngr


def parse_file_name(file_name: str = 'test_file.yml') -> str:
    """
    Returns the path to the yaml file needed to parse.
        Args:
            file_name: name of the yaml file to parse
        Return:
           path to yaml file needed to parse as string
    """
    script_location = Path(__file__).parent
    return f"{script_location}/{file_name}"


def run_game_iterations(board: list[list[Entity]], turns_int_game: int) -> None:
    """
    Function to run entire game turns as wanted.
    Args:
        board: initial game board
        turns_int_game:  total turns the game would run in
    """
    for current_turn in range(1, turns_int_game + 1):
        print("current turn: " + str(current_turn))
        board.update_game_board()
        board.print_game_board()
        board.print_counter_of_all_entities()


if __name__ == '__main__':
    total_turns = int(input("Enter number of turns: "))
    game_manager = init_event_manger()
    sign_users_to_events(game_manager)
    game_board = GameBoard(game_manager)
    print("starting board position:")
    game_board.print_game_board()
    run_game_iterations(game_board, total_turns)
    game_manager.notify("game finished")
