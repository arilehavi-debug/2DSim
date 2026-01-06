"""
this module contains abstract class entity
"""
from abc import ABC, abstractmethod


class Entity(ABC):
    """
    abstract class for type "Entity"
    contains all signatures for needed functions to object of type "Entity"
    """

    @abstractmethod
    def update_life_span(self, new_life_span: int) -> None:
        """updating the entity's life span

                Args:
                    new_life_span: new total life span of the entity
        """

    @abstractmethod
    def update_location(self, new_location: tuple[int, int]) -> None:
        """updating the entity's location on board

                Args:
                    new_location: new location of the entity
        """

    @abstractmethod
    def update_iteration(self, curr_board: list[list], location: tuple[int, int]) -> None:
        """updating the entity's properties in a certain
            iteration over the entire board
            we make sure to update the entity's location and life span
            and affect other cells in the board

                Args:
                    curr_board: representation of all cells in the board
                    location: representation of the entity's current location in the game board
        """
