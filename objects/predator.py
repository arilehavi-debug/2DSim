from objects.herbivore import Herbivore
from objects.entity import Entity
from objects.mobile_entity import MobileEntity
from lib_consts.const_file import T_PREDATOR, R_PREDATOR_SIGHT
from event_handling.event_manager import EventManager


class Predator(MobileEntity):
    """
    Class for type "Predator"
    Contains all signatures for needed functions to object of type "Predator"
    """

    def __init__(self, location: tuple[int, int], life_span: int = T_PREDATOR):
        """
         Constructor that initializes the class
        """
        self.life_span = life_span
        self.location = location

    def update_iteration(self, curr_board: list[list[Entity]], location: tuple[int, int],
                         mngr: EventManager) -> None:
        """Updating the Predator entity after every iteration
            Args:
                curr_board: current board of the game
                location: tuple representing the current cell a predator is in

        """
        optional_loc = self.determine_next_location(curr_board, location,
                                                    R_PREDATOR_SIGHT, Herbivore)

        if self.check_if_needed_to_refuel_life_span(curr_board, optional_loc[0], optional_loc[1],
                                                    Herbivore):
            self.life_span = T_PREDATOR

        self.update_location_in_game_board(curr_board, location, optional_loc, mngr)
        self.life_span -= 1
