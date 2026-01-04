import random as rnd
# CONSTANTS FOR THE ENTIRE PROGRAM
T_Plant = 0
T_herbivore = 0
T_predator = 0
R_herbivore_sight = 0
R_predator_sight = 0

def kill_entity(curr_board, location):
    del curr_board[location[0]][location[1]]
    curr_board[location[0]][location[1]] = None


def check_plant_in_radius():
    pass


class BasicEntity:
    # a basic class for all instances in the program
    life_span = 0 # current life span of the object
    location = () # current location of the object in the board
    def __init__(self, location, life_span):
        self.life_span = life_span
        self.location = location

    def update_life_span(self, new_life_span):
        self.life_span = new_life_span

    def update_location(self, new_location):
        self.location = new_location

    def update_iteration(self, curr_board, location):
            raise Exception("NotImplementedException")

class Plant (BasicEntity):
    def __init__(self, location):
        self.life_span = T_Plant
        self.location = location

    # a basic class for all instances in the program
    def update_iteration(self, curr_board, location):
        self.life_span -= 1
        # in case it's time for the plant to terminate itself
        if self.life_span == 0:
            self.kill_entity(curr_board, location)
            create_new_entity(curr_board, location)


class Herbivore(BasicEntity):
    def __init__(self, location):
        self.life_span = T_herbivore
        self.location = location

    # a basic class for all instances in the program
    def update_iteration(self, curr_board, location):
        self.life_span -= 1

        if self.life_span == 0:
            self.kill_entity(curr_board, location)
            create_new_entity(curr_board, location)



class Predator(BasicEntity):
    def __init__(self, location):
        self.life_span = T_predator
        self.location = location

    # a basic class for all instances in the program
    def update_predator_location(self, current_table):
        pass