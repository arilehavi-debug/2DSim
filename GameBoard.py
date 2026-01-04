import MobileEntity
import yaml
import random
from numpy.f2py.auxfuncs import throw_error

MESSAGE_NO_OBJECTS_OF_TYPE_LEFT = "Alert! there aren't any objects left of type: "

def parse_config_file(config_file_name):
    try:
        with open(config_file_name, 'r') as f:
            return yaml.safe_load(f)

    except FileNotFoundError:
        throw_error(FileNotFoundError)

def init_live_objects_counter(config_dict):
    object_ctr_dict = {}
    for i in range(len(config_dict["TypesStrings"])):
        object_ctr_dict[i] = 0
    return object_ctr_dict

class GameBoard:
    const_dict = {}
    live_objects_counter = {} #format of counters is number to represent the type

    def __init__(self, rows, cols, route_to_config_file):
        self.const_dict = parse_config_file(route_to_config_file)
        self.live_objects_counter = init_live_objects_counter(self.const_dict)
        self.board = []

        # we make sure to create the game board
        # as a 2D array of Entities
        for row in range(rows):
            self.board.append([])
            for col in range(cols):
                # drill a random entity to init the game board
                # select a type to initiate of
                curr_type = random.randint(1, len(self.const_dict["Types"]))
                self.board[-1].append(
                    self.const_dict["Types"][random]((row, col),
                                                     self.const_dict["LifeSpan"][curr_type]))
                # update counter for live objects of a certain type
                self.live_objects_counter[curr_type] += 1

    def check_if_entity_life_span_ended(self, row, col):
        if (self.board[row][col].life_span - 1) == 0:
            self.board[row][col].update_life_span(0)
            return True
        return False

    def update_game_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.check_if_entity_life_span_ended(row,col):
                    # in case the entity's life span ended
                    # we update the lives counter and add another entity
                    

                # if the object should terminate itself


