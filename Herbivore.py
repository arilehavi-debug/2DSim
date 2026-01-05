from  MobileEntity import MobileEntity
from ConstFile import Prog_constants
from Plant import Plant

class Herbivore(MobileEntity):

    def __init__(self, location, life_span):
        self.life_span = life_span
        self.location = location
        self.curr_cooldown_time = 0

    def __init__(self, location):
        self.life_span = Prog_constants.T_HERBIVORE
        self.location = location
        self.curr_cooldown_time = 0

    def update_life_span(self, new_life_span):
        self.life_span = new_life_span

    def update_location(self, new_location):
        self.location = new_location

    def create_new_herbivore(self, curr_board, location):
        curr_board[location[0]][location[1]] = Herbivore(location)

    # a basic class for all instances in the program
    def update_iteration(self, curr_board, location):
        # check where the closest plant is
        optional_loc = self.determine_next_location(curr_board, location, Prog_constants.R_HERBIVORE_SIGHT, Plant)
        # if the position we got to is a Plant, we refuel our life span
        if self.check_if_needed_to_refuel_life_span(curr_board, optional_loc[0], optional_loc[1],
                                                    Plant):
            self.life_span = Prog_constants.T_HERBIVORE

        # if we got to another Herbivore, we check that we can reproduce
        if self.check_if_needed_to_refuel_life_span(curr_board, optional_loc[0], optional_loc[1],
                                                    Herbivore):
            if self.curr_cooldown_time == 0:
                self.curr_cooldown_time = Prog_constants.T_COOLDOWN
                # create herbivore in nearing cell
                new_herbivore_location = self._get_random_nearing_location_in_board(curr_board, optional_loc)
                self.create_new_herbivore(curr_board, new_herbivore_location)

        self.update_location_in_game_board(curr_board, location, optional_loc)
        # update spans:
        self.life_span -= 1
        if self.curr_cooldown_time > 0:
            self.curr_cooldown_time -= 1
