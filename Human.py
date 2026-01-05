from Predator import Predator
from ConstFile import Prog_constants
from MobileEntity import MobileEntity

class Human(MobileEntity):
        def __init__(self, location, life_span):
            self.life_span = life_span
            self.location = location

        def __init__(self, location):
            self.life_span = Prog_constants.T_HUMAN
            self.location = location

        def update_life_span(self, new_life_span):
            self.life_span = new_life_span

        # a basic class for all instances in the program
        def update_iteration(self, curr_board, location):

            optional_loc = self.determine_next_location(curr_board, location, Prog_constants.R_HUMAN_SIGHT, Predator)
            if self.check_if_needed_to_refuel_life_span(curr_board, optional_loc[0], optional_loc[1],
                                                        Predator):
                self.life_span = Prog_constants.T_HUMAN

            # if we got to another Herbivore, we check that we can reproduce
            if self.check_if_needed_to_refuel_life_span(curr_board, optional_loc[0], optional_loc[1],
                                                        Human):
                    # create herbivore in two nearing cells
                    new_human_location_1 = self._get_random_nearing_location_in_board(curr_board, optional_loc)
                    new_human_location_2 = self._get_random_nearing_location_in_board(curr_board, optional_loc)
                    while new_human_location_1 == new_human_location_2:
                        new_human_location_2 = self._get_random_nearing_location_in_board(curr_board, optional_loc)

                    curr_board[new_human_location_1[0]][new_human_location_1[1]] = Human(new_human_location_1)
                    curr_board[new_human_location_2[0]][new_human_location_2[1]] = Human(new_human_location_2)

            self.update_location_in_game_board(curr_board, location, optional_loc)

            self.life_span -= 1
