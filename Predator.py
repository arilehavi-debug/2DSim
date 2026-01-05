from Herbivore import Herbivore
from MobileEntity import MobileEntity
import numpy as np
from ConstFile import Prog_constants

class Predator(MobileEntity):

    def __init__(self, location, life_span):
        self.life_span = life_span
        self.location = location

    def __init__(self, location):
        self.life_span = Prog_constants.T_PREDATOR
        self.location = location

    def update_life_span(self, new_life_span):
        self.life_span = new_life_span

    # a basic class for all instances in the program
    def update_iteration(self, curr_board, location):
        # check where the closest herbivore is
        optional_loc = self.determine_next_location(curr_board, location, Prog_constants.R_PREDATOR_SIGHT, Herbivore)

        # if the position we got to is a herbivore, we refuel our life span
        if self.check_if_needed_to_refuel_life_span(curr_board, optional_loc[0], optional_loc[1],
                                                    Herbivore):
            self.life_span = Prog_constants.T_PREDATOR

        self.update_location_in_game_board(curr_board, location, optional_loc)
        # update spans:
        self.life_span -= 1
