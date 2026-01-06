"""
module contains GameBoard class
"""
import random
import yaml
from board_consts import CONST_DICT, PRINT_DICT, TYPE_CODING, STR_TYPE_DICT
from entity import Entity
from plant import Plant


class GameBoard:
    """
    class of type "GameBoard"
    holds a board of entities and updates the game from beginning to end
    """

    def __init__(self):
        """
         constructor that initializes the class
        """
        self.live_objects_counter = {CONST_DICT[i]: 0 for i in range(1, len(CONST_DICT) + 1)}
        self.board = self.create_board_from_yaml("test_file.yml")

    def create_board_from_yaml(self, filename: str) -> list[list[Entity]]:
        """creating game board from yaml file

                Args:
                    filename: name of the yaml file to upload.

                Returns:
                   2D array of entities representing all objects in game.

                """

        with open(filename, 'r', encoding="utf-8") as file:
            yaml_string = yaml.safe_load(file)

        board_by_rows = yaml_string["Board Configuration"]
        board_by_rows = board_by_rows.split("\n")

        board = [
            [
                TYPE_CODING[cell]((row, col))
                for col, cell in enumerate(row_data)
            ]
            for row, row_data in enumerate(board_by_rows)
        ]

        return board

    def check_if_entity_life_span_ended(self, row: int, col: int) -> bool:
        """checking if the entity's life span ended and needed return

                Args:
                    row: row of cell.
                    col: column of cell.

                Returns:
                   "True" if the cell's life span ended and "False" otherwise.

                """
        if self.board[row][col].life_span == 0:
            return True
        return False

    def fill_with_plants_if_needed(self) -> None:
        """after every iteration go through all empty spaces and randomly place plants
                """
        self.board = [
            [
                Plant((row, col)) if self.board[row][col] is None and random.randint(1, 2) == 1
                else self.board[row][col]
                for col in range(len(self.board[0]))
            ]
            for row in range(len(self.board))
        ]

    def print_counter_of_all_entities(self) -> None:
        """
        print number of every entity in the game after every iteration
        """
        for i in range(1, len(STR_TYPE_DICT) + 1):
            print("Total entities from type " + STR_TYPE_DICT[i] + ": " +
                  str(self.live_objects_counter[CONST_DICT[i]]))

    def update_game_life_counter(self) -> None:
        """
        update the list contains number of all existing entities on board from every type
        """
        for key in self.live_objects_counter.keys():
            self.live_objects_counter[key] = 0

        for row, curr_row in enumerate(self.board):
            for col, curr_cell in enumerate(curr_row):
                if curr_cell is not None:
                    self.live_objects_counter[type(self.board[row][col])] += 1

    def print_game_board(self) -> None:
        """
         print all elements in the game board without delimiters on screen
        """
        for curr_row in self.board:
            for curr_cell in curr_row:
                print(PRINT_DICT[type(curr_cell)], end="")
            print("\n", end="")

    def update_game_board(self) -> None:
        """
        function to update entire game board by going through every cell in the board
        """
        for idx_row, row in enumerate(self.board):
            for idx_col, cell in enumerate(row):
                if self.board[idx_row][idx_col] is not None:
                    if self.check_if_entity_life_span_ended(idx_row, idx_col):
                        self.board[idx_row][idx_col] = None
                    else:
                        cell.update_iteration(self.board, (idx_row, idx_col))

        self.fill_with_plants_if_needed()
        self.update_game_life_counter()
