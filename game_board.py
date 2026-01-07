import random
from types import NoneType

import yaml

from lib_consts.board_consts import CONST_DICT, PRINT_DICT, \
                                     TYPE_CODING, STR_TYPE_DICT, TEST_FILE_NAME
from objects.entity import Entity
from objects.plant import Plant
from event_handling.event_managaer import EventManager

class GameBoard:
    """
    Class of type "GameBoard"
    Holds a board of entities and updates the game from beginning to end
    """

    def __init__(self, mngr: EventManager):
        """
         Constructor that initializes the class
        """
        self.live_objects_counter = dict.fromkeys(PRINT_DICT.keys(), 0)
        self.mngr = mngr
        self.board = self.create_board_from_yaml(TEST_FILE_NAME)

    def create_board_from_yaml(self, filename: str) -> list[list[Entity]]:
        """
        creating game board from yaml file
        Args:
            filename: name of the yaml file to upload.
        Returns:
           2D array of entities representing all objects in game.
        """

        with open(filename, 'r', encoding="utf-8") as file:
            yaml_string = yaml.safe_load(file)

        board_by_rows = yaml_string["Board Configuration"]
        board_by_rows = board_by_rows.split("\n")

        board = []
        for row, row_data in enumerate(board_by_rows):
            board.append([])
            for col, cell in enumerate(row_data):
                board[-1].append(TYPE_CODING[cell](row, col))
                self.mngr.notify("entity added or reduced",
                                 type=TYPE_CODING[cell], factor="added")
        return board

    def check_if_entity_life_span_ended(self, row: int, col: int) -> bool:
        """Checking if the entity's life span ended and needed return
            Args:
                row: row of cell.
                col: column of cell.
            Returns:
               "True" if the cell's life span ended and "False" otherwise.
                """
        return self.board[row][col].life_span == 0

    def fill_with_plants_if_needed(self) -> None:
        """
        After every iteration go through all empty spaces and randomly place plants
        """
        self.board = [
            [
                Plant((row, col)) if
                self.board[row][col] is None and
                random.randint(1, 2) == 1 else self.board[row][col]
                for col in range(len(self.board[0]))
            ]
            for row in range(len(self.board))
        ]

    def print_counter_of_all_entities(self) -> None:
        """
        Print number of every entity in the game after every iteration
        """
        for i in range(1, len(STR_TYPE_DICT) + 1):
            print(f"Total entities from type {STR_TYPE_DICT[i]} :"
                  f" {self.live_objects_counter[CONST_DICT[i]]}")

    def update_game_life_counter(self, event_manager: EventManager) -> None:
        """
        Update the list contains number of all existing entities on board from every type
        """
        self.live_objects_counter = dict.fromkeys(self.live_objects_counter.keys(), 0)
        for row in self.board:
            for cell in row:
                if cell is not None:
                    self.live_objects_counter[type(cell)] += 1
                self.mngr.notify("entity added or reduced", type=type(cell), factor="added")


        # checking if there are entities that aren't left in board
        for key in self.live_objects_counter.keys():
            if self.live_objects_counter[key] == 0 and key is not NoneType:
                event_manager.notify("no more entities left",
                                     data=f"No more entities left of type: {key}")

    def print_game_board(self) -> None:
        """
         Print all elements in the game board without delimiters on screen
        """
        for curr_row in self.board:
            for curr_cell in curr_row:
                print(PRINT_DICT[type(curr_cell)], end="")
            print("\n", end="")

    def check_precentage_of_plants(self, event_manager: EventManager) -> None:
        total_plants = 0
        for row in self.board:
            for cell in row:
                if type(cell) is Plant:
                    total_plants += 1

        if total_plants > 0.9 * len(self.board) * len(self.board[0]):
            event_manager.notify("plant percentage exceeds 90 percent",
                                 data="Number of plants is bigger then 90 percents of board")

    def update_game_board(self) -> None:
        """
        Function to update entire game board by going through every cell in the board
        """
        self.mngr.notify("iteration ended")
        for idx_row, row in enumerate(self.board):
            for idx_col, cell in enumerate(row):
                if self.board[idx_row][idx_col] is not None:
                    if self.check_if_entity_life_span_ended(idx_row, idx_col):
                        self.board[idx_row][idx_col] = None
                    else:
                        cell.update_iteration(self.board, (idx_row, idx_col), self.mngr)

        self.fill_with_plants_if_needed()
        self.update_game_life_counter(self.mngr)
        self.check_precentage_of_plants(self.mngr)
