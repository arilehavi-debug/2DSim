"""
this module contains class Human
"""
from entity import Entity
from predator import Predator
from const_file import T_HUMAN, R_HUMAN_SIGHT
from mobile_entity import MobileEntity


class Human(MobileEntity):
    """
    class for type "Human"
    contains all signatures for needed functions to object of type "Human"
    """

    def __init__(self, location: tuple[int, int], life_span: int = T_HUMAN):
        """
         constructor that initializes the class
        """
        self.life_span = life_span
        self.location = location

    def update_iteration(self, curr_board: list[list[Entity]], location: tuple[int, int]) -> None:
        """updating the Human entity after every iteration

                Args:
                    curr_board: current board of the game
                    location: tuple representing the cell to create a new herbivore in

        """
        optional_loc = self.determine_next_location(curr_board, location, R_HUMAN_SIGHT, Predator)
        if self.check_if_needed_to_refuel_life_span(curr_board, optional_loc[0], optional_loc[1],
                                                    Predator):
            self.life_span = T_HUMAN

        if self.check_if_needed_to_refuel_life_span(curr_board, optional_loc[0], optional_loc[1],
                                                    Human):

            new_human_location_1 = (
                self._get_random_nearing_location_in_board(curr_board, optional_loc))
            new_human_location_2 = (
                self._get_random_nearing_location_in_board(curr_board, optional_loc))
            while new_human_location_1 == new_human_location_2:
                new_human_location_2 = \
                    self._get_random_nearing_location_in_board(curr_board, optional_loc)

            curr_board[new_human_location_1[0]][new_human_location_1[1]] = \
                Human(new_human_location_1)
            curr_board[new_human_location_2[0]][new_human_location_2[1]] = \
                Human(new_human_location_2)

        self.update_location_in_game_board(curr_board, location, optional_loc)

        self.life_span -= 1
