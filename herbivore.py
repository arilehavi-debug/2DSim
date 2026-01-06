"""
this module contains class Herbivore
"""
from mobile_entity import MobileEntity
from entity import Entity
from const_file import R_HERBIVORE_SIGHT, T_HERBIVORE, T_COOLDOWN
from plant import Plant


class Herbivore(MobileEntity):
    """
    class for type "Herbivore"
    contains all signatures for needed functions to object of type "Herbivore"
    """

    def __init__(self, location: tuple[int, int], life_span: int = T_HERBIVORE):
        """
         constructor that initializes the class
        """
        self.life_span = life_span
        self.location = location
        self.curr_cooldown_time = 0

    def create_new_herbivore(self, curr_board: list[list[Entity]], location: tuple[int, int]) \
            -> None:
        """creating a new herbivore in a different location

                Args:
                    curr_board: current board of the game
                    location: tuple representing the cell to create a new herbivore in

        """
        curr_board[location[0]][location[1]] = Herbivore(location)

    def update_iteration(self, curr_board: list[list[Entity]], location: tuple[int, int]) -> None:
        """updating the herbivore entity after every iteration

                Args:
                    curr_board: current board of the game
                    location: tuple representing the current cell a herbivore is in

        """
        optional_loc = self.determine_next_location(curr_board, location, R_HERBIVORE_SIGHT, Plant)
        if self.check_if_needed_to_refuel_life_span(curr_board, optional_loc[0], optional_loc[1],
                                                    Plant):
            self.life_span = T_HERBIVORE

        if self.check_if_needed_to_refuel_life_span(curr_board, optional_loc[0], optional_loc[1],
                                                    Herbivore):
            if self.curr_cooldown_time == 0:
                self.curr_cooldown_time = T_COOLDOWN
                new_herbivore_location = (
                    self._get_random_nearing_location_in_board(curr_board, optional_loc))
                self.create_new_herbivore(curr_board, new_herbivore_location)

        self.update_location_in_game_board(curr_board, location, optional_loc)
        self.life_span -= 1
        if self.curr_cooldown_time > 0:
            self.curr_cooldown_time -= 1
