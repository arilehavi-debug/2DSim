from Entity import Entity
import random as rnd
import numpy as np

class MobileEntity(Entity):
    life_span = 0
    location = ()

    def __init__(self, location, life_span):
        self.life_span = life_span
        self.location = location

    def update_life_span(self, new_life_span):
        self.life_span = new_life_span

    def update_location(self, new_location):
        self.location = new_location

    def update_iteration(self, curr_board, location):
        pass

    def _check_valid_coordinates(self, curr_board, curr_row, curr_col):
        return (curr_row >= 0 and curr_col >= 0 and curr_row < len(curr_board)
                and curr_col < len(curr_board[0]))

    def _parse_new_location_after_finding_an_instance(self, location, plant_location):
        return (location[0] + np.sign(plant_location[0] - location[0]),
                location[1] + np.sign(plant_location[1] - location[1]))

    def _get_new_position_if_type_found(self, curr_board, type_to_find, prev_loc, loc_row, loc_col):
        if self._check_valid_coordinates(curr_board, loc_row, loc_col):
            if isinstance(curr_board[loc_row][loc_col], type_to_find):
                return self._parse_new_location_after_finding_an_instance(prev_loc,
                                                                           (loc_row,
                                                                            loc_col))
        return None

    def _find_closest_entity(self, curr_board, location, radius_to_search, type_to_find):
        # run through the entire board
        # until we get to a plant
        optional_loc = None
        for addition_factor in range(1, radius_to_search + 1):
            for curr_add in range(-1 * addition_factor, addition_factor + 1):
                optional_loc = self._get_new_position_if_type_found(
                    curr_board, type_to_find, location, location[0] + addition_factor, location[1] + curr_add)
                if optional_loc is not None:
                        return optional_loc

                optional_loc = self._get_new_position_if_type_found(
                    curr_board, type_to_find, location, location[0] - addition_factor, location[1] + curr_add)
                if optional_loc is not None:
                        return optional_loc

                optional_loc = self._get_new_position_if_type_found(
                    curr_board, type_to_find, location, location[0] + curr_add, location[1] - addition_factor)
                if optional_loc is not None:
                    return optional_loc

                optionl_loc = self._get_new_position_if_type_found(
                    curr_board, type_to_find, location, location[0] + curr_add, location[1] + addition_factor
                )
                if optionl_loc is not None:
                    return optionl_loc

        return optional_loc

    def _get_random_nearing_location_in_board(self, curr_board, location):
        min_row = max(0, location[0] - 1)
        max_row = min(len(curr_board) - 1, location[0] + 1)
        min_col = max(0, location[1] - 1)
        max_col = min(len(curr_board[0]) - 1, location[1] + 1)
        return (rnd.randint(min_row, max_row),
                rnd.randint(min_col, max_col))

    def determine_next_location(self, curr_board, location, radius_to_search, type_to_find):
        curr_loc = self._find_closest_entity(curr_board, location, radius_to_search, type_to_find)
        if curr_loc is not None:
            return curr_loc
        else:
            # drill a random location that the plant will be put in
            # make sure that it's inside the game board
            return self._get_random_nearing_location_in_board(curr_board, location)

    def check_if_needed_to_refuel_life_span(self, curr_board, curr_row, curr_col, type_to_check):
        return isinstance(curr_board[curr_row][curr_col], type_to_check)

    def update_location_in_game_board(self, curr_board, curr_location, new_location):
        # release all memory of the board with our new location
        curr_board[new_location[0]][new_location[1]] = self
        curr_board[curr_location[0]][curr_location[1]] = None
        self.location = new_location
