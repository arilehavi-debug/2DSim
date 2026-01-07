import random as rnd
import numpy as np

from objects.entity import Entity


class MobileEntity(Entity):
    """
    Class that represents a mobile entity
    Holds the options to move around the game board
    """
    life_span = 0
    location = ()

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

    def _check_valid_coordinates(self, curr_board: list[list[Entity]],
                                 curr_row: int, curr_col: int) -> bool:
        """
        Function to check if coordinates are inside board
        Args:
            curr_board: board game
            curr_row: row to check
            curr_col: colum to check
        Return:
            "true" if location in board, "false" otherwise
        """
        return len(curr_board) > curr_row >= 0 and len(curr_board[0]) > curr_col >= 0

    def _parse_new_location_after_finding_an_instance(self, location: tuple[int, int],
                                                      plant_location: tuple[int, int]) \
            -> tuple[int, int]:
        """
        After finding a location of a wanted type, we make sure to return the closest
        Args:
            location: tuple indicating instance's location
            plant_location: the location we need to look for
        Return:
             location adjacent to the current one closest to the plant location
        """
        return (location[0] + np.sign(plant_location[0] - location[0]),
                location[1] + np.sign(plant_location[1] - location[1]))

    def _get_new_position_if_type_found(self, curr_board: list[list[Entity]],
                                        type_to_find: type, prev_loc: tuple[int, int],
                                        location_find: tuple[int, int]) -> tuple[int, int] or None:
        """
        Finding an instance of type we're looking for to return the object
        of type we are looking for
        Args:
            curr_board: current game board
            type_to_find: type we are trying to search
            prev_loc: previous location we were looking for
            location_find: location to search if we return or not
        Return:
             new location after finding the object we're looking for, None otherwise
        """
        if self._check_valid_coordinates(curr_board, location_find[0], location_find[1]) and \
                isinstance(curr_board[location_find[0]][location_find[1]], type_to_find):
            return self._parse_new_location_after_finding_an_instance(prev_loc,
                                                                      (location_find[0],
                                                                       location_find[1]))
        return None

    def _find_closest_entity(self, curr_board: list[list[Entity]], location: tuple[int, int],
                             radius_to_search: int, type_to_find: type) -> tuple[int, int] or None:
        """
        Finding closest wanted entity from type "type to find" to our location
        Parameters:
            curr_board: current game board
            location: location to search from
            radius_to_search: radius we want to search in
            type_to_find: object type to look for
        Return:
             closest entity we found or None if we haven't found it
        """
        optional_loc = None
        for addition_factor in range(1, radius_to_search + 1):
            for curr_add in range(-1 * addition_factor, addition_factor + 1):
                optional_loc = self._get_new_position_if_type_found(
                    curr_board, type_to_find, location,
                    (location[0] + addition_factor, location[1] + curr_add))
                if optional_loc is not None:
                    return optional_loc

                optional_loc = self._get_new_position_if_type_found(
                    curr_board, type_to_find, location,
                    (location[0] - addition_factor, location[1] + curr_add))
                if optional_loc is not None:
                    return optional_loc

                optional_loc = self._get_new_position_if_type_found(
                    curr_board, type_to_find, location,
                    (location[0] + curr_add, location[1] - addition_factor))
                if optional_loc is not None:
                    return optional_loc

                optional_loc = self._get_new_position_if_type_found(
                    curr_board, type_to_find, location,
                    (location[0] + curr_add, location[1] + addition_factor))

                if optional_loc is not None:
                    return optional_loc

        return optional_loc

    def _get_random_nearing_location_in_board(self, curr_board: list[list[Entity]],
                                              location: tuple[int, int]) -> tuple[int, int]:
        """
        Drill random location inside board next to the location and return it
        Args:
            curr_board: current game board
            location: current location inside board
        Return:
             random location next to the current one
        """
        min_row = max(0, location[0] - 1)
        max_row = min(len(curr_board) - 1, location[0] + 1)
        min_col = max(0, location[1] - 1)
        max_col = min(len(curr_board[0]) - 1, location[1] + 1)
        return (rnd.randint(min_row, max_row),
                rnd.randint(min_col, max_col))

    def determine_next_location(self, curr_board: list[list[Entity]],
                                location: tuple[int, int],
                                radius_to_search: int, type_to_find: type) \
            -> tuple[int, int] or None:
        """
        Function to return next location in board we are looking for
        If we found an object of type "type to find" we return its position,
        else we drill a random nearing location and return it
        Args:
            curr_board: current game board
            location: current location
            radius_to_search: radius to search for an entity from type "type to find"
            type_to_find: type to search for
        Return:
             next location in board
        """
        curr_loc = self._find_closest_entity \
            (curr_board, location, radius_to_search, type_to_find)
        if curr_loc is not None:
            return curr_loc
        return self._get_random_nearing_location_in_board(curr_board, location)

    def check_if_needed_to_refuel_life_span(self, curr_board: list[list[Entity]], curr_row: int,
                                            curr_col: int, type_to_check: type) -> bool:
        """
        Return "true" if we found an object that demands refueling life span, false otherwise
        Args:
            curr_board: current game board
            curr_row: int
            curr_col: int
            type_to_check: type we want to search for
        Return:
             "true" if life refueling needed, "false" otherwise
        """
        return isinstance(curr_board[curr_row][curr_col], type_to_check)

    def update_location_in_game_board(self, curr_board: list[list[bool]],
                                      curr_location: tuple[int, int],
                                      new_location: tuple[int, int]) -> None:
        """
        Updating entity's location
        Args:
            curr_board: current game board
            curr_location: current location of object
            new_location: new location of object
        """
        curr_board[new_location[0]][new_location[1]] = self
        curr_board[curr_location[0]][curr_location[1]] = None
        self.location = new_location
