"""
this module contains class Plant
"""
from entity import Entity
from const_file import T_PLANT


class Plant(Entity):
    """
    class for type "Plant"
    contains all signatures for needed functions to object of type "Plant"
    """

    def __init__(self, location: tuple[int, int], life_span: int = T_PLANT):
        """
         constructor that initializes the class
        """
        self.life_span = life_span
        self.location = location

    # a basic class for all instances in the program
    def update_iteration(self, curr_board: list[list[Entity]], location: tuple[int, int]) -> None:
        """updating the plant entity after every iteration

                Args:
                    curr_board: current board of the game
                    location: tuple representing the current cell a herbivore is in

        """
        self.life_span -= 1
