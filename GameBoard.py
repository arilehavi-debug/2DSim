from types import NoneType

from Plant import Plant
from Human import Human
from Predator import Predator
from Herbivore import Herbivore
from BoardConsts import BoardConsts
import yaml
import random

class GameBoard:

    def __init__(self):
        self.live_objects_counter = {Plant: 0, Herbivore: 0, Predator: 0, Human: 0}
        self.board = self.create_board_from_yaml("test_file.yml")

    def create_board_from_yaml(self,filename):
        board = []
        yaml_string = ""
        with open(filename, 'r') as file:
            yaml_string = yaml.safe_load(file)

        board_by_rows = yaml_string["Board Configuration"]
        board_by_rows = board_by_rows.split("\n")

        for row in range(len(board_by_rows)):
            board.append([])
            for col in range(len(board_by_rows[row])):
                board[-1].append(BoardConsts.TYPE_CODING[board_by_rows[row][col]]((row, col)))

        return board

    def check_if_entity_life_span_ended(self, row, col):
        if self.board[row][col].life_span == 0:
            return True
        return False

    def fill_with_plants_if_needed(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == None:
                    # drill if we want to create a Plant or not
                    if random.randint(1, 2) == 1:
                        self.board[row][col] = Plant((row, col))

    def print_counter_of_all_entities(self):
        for i in range(1, len(BoardConsts.STR_TYPE_DICT) + 1):
            print("Total entities from type " + BoardConsts.STR_TYPE_DICT[i] +": " +
                  str(self.live_objects_counter[BoardConsts.CONST_DICT[i]]))

    def update_game_life_counter(self):
        # nullify all organs
        for key in self.live_objects_counter.keys():
            self.live_objects_counter[key] = 0

        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == None:
                    # drill if we want to create a Plant or not
                    if random.randint(1, 2) == 1:
                        self.board[row][col] = Plant((row, col))
                        self.live_objects_counter[type(self.board[row][col])] += 1
                else:
                    self.live_objects_counter[type(self.board[row][col])] += 1

    def print_game_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                    print(BoardConsts.PRINT_DICT[type(self.board[row][col])], end="")
            print("\n", end="")

    def update_game_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] != None:
                    if self.check_if_entity_life_span_ended(row,col):
                        # in case the entity's life span ended
                        # we update the board and turn it to None
                        self.board[row][col] = None
                    else:
                        self.board[row][col].update_iteration(self.board, (row, col))

        # update live objects counter of any type
        # decide if to drill a Plant or not
        self.fill_with_plants_if_needed()
        self.update_game_life_counter()