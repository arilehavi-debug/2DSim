from abc import ABC, abstractmethod

from event_handling.event_manager import EventManager


class Entity(ABC):
    """
    Abstract class for type "Entity".
    Contains all signatures for needed functions to object of type "Entity".
    """

    @abstractmethod
    def update_life_span(self, new_life_span: int) -> None:
        """
        Updating the entity's life span.

            Args:
                new_life_span: new total life span of the entity
        """

    @abstractmethod
    def update_location(self, new_location: tuple[int, int]) -> None:
        """
        Updating the entity's location on board.

            Args:
                new_location: new location of the entity
        """

    @abstractmethod
    def update_iteration(self, curr_board: list[list], location: tuple[int, int],
                         event_manager: EventManager) -> None:
        """
        Updating the entity's properties in a certain
        iteration over the entire board.
        We make sure to update the entity's location and life span
        and affect other cells in the board.

            Args:
                curr_board: representation of all cells in the board
                location: representation of the entity's current location in the game board
        """
