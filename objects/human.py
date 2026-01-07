from objects.entity import Entity
from objects.predator import Predator
from lib_consts.const_file import T_HUMAN, R_HUMAN_SIGHT
from objects.mobile_entity import MobileEntity
from event_handling import EventManager


class Human(MobileEntity):
    """
    Class for type "Human"
    Contains all signatures for needed functions to object of type "Human"
    When a human reaches a predator, it consumes the predator - refueling his life span
    When a human reaches another human, it multiplies - and creates 2 new humans in random
    nearing location
    """

    def __init__(self, location: tuple[int, int], life_span: int = T_HUMAN):
        """
         Constructor that initializes the class
        """
        self.life_span = life_span
        self.location = location

    def update_iteration(self, curr_board: list[list[Entity]], location: tuple[int, int],
                         event_manager: EventManager) -> None:
        """Updating the Human entity after every iteration
            When he reaches a predator, he consumes it - refueling his life span
            When he reaches another human, he multiplies - and creates 2 new humans in
            random nearing locations

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

            new_human_created_1 = (
                self._get_random_nearing_location_in_board(curr_board, optional_loc))
            new_human_created_2 = (
                self._get_random_nearing_location_in_board(curr_board, optional_loc))
            while new_human_created_1 == new_human_created_2:
                new_human_created_2 = \
                    self._get_random_nearing_location_in_board(curr_board, optional_loc)

            curr_board[new_human_created_1[0]][new_human_created_1[1]] = \
                Human(new_human_created_1)
            curr_board[new_human_created_2[0]][new_human_created_2[1]] = \
                Human(new_human_created_2)

        self.update_location_in_game_board(curr_board, location, optional_loc)

        self.life_span -= 1
