from objects.entity import Entity
from lib_consts.const_file import T_PLANT
from event_handling.event_managaer import EventManager


class Plant(Entity):
    """
    Class for type "Plant"
    Contains all signatures for needed functions to object of type "Plant"
    """

    def __init__(self, location: tuple[int, int], life_span: int = T_PLANT):
        """
         Constructor that initializes the class
        """
        self.life_span = life_span
        self.location = location

    def update_life_span(self, new_life_span: int) -> None:
        """
        Updating entity's life span
        Args:
             new_life_span: new life span of the object
        """
        self.life_span = new_life_span

    def update_location(self, new_location: tuple[int, int]) -> None:
        """
        Updating entity's location in board
        Args:
             new_location: represent location of entity
        """
        self.location = new_location

    def update_iteration(self, curr_board: list[list[Entity]], location: tuple[int, int],
                         event_manager: EventManager) -> None:
        """Updating the plant entity after every iteration
            Args:
                curr_board: current board of the game
                location: tuple representing the current cell a herbivore is in

        """
        self.life_span -= 1
