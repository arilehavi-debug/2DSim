import random as rnd
# CONSTANTS FOR THE ENTIRE PROGRAM
T_Plant = 0
T_herbivore = 0
T_predator = 0
R_herbivore_sight = 0
R_predator_sight = 0
NO_MORE_PLANTS_MESSAGE = "There aren't any plants left on the board!"
NO_MORE_HERBIVORES_MESSAGE = "There aren't any herbivores left on the board!"
NO_MORE_PREDATORS_MESSAGE = "There aren't any predators left on the board!"
PLANT_PERCENTAGE_EXCEEDS_90_PERCENTS = "The amount of plants exceeds 90 percents of the board"

# global variables
total_plants_counter = 0
total_herbivores_counter = 0
total_predators_counter = 0

def create_new_entity(curr_board, location):
    global total_plants_counter
    global total_herbivores_counter
    global total_predators_counter
    # drill a random entity to put instead of the last one
    # that got terminated

    type = rnd.randint(1,3)

    if type == 1:
        curr_board[location[0]][location[1]] = Plant(location)

    elif type == 2:
        curr_board[location[0]][location[1]] = Herbivore(location)

    elif type == 3:
        curr_board[location[0]][location[1]] = Predator(location)

# in case an entity dies, we create a new plant in its location
def create_plant_in_new_position(curr_board, location):
    global total_plants_counter
    curr_board[location[0]][location[1]] = Plant(location)

def kill_entity(curr_board, location):
    curr_board[location[0]][location[1]] = None

def check_if_there_are_zero_entities():
    global total_plants_counter
    global total_herbivores_counter
    global total_predators_counter

    if total_plants_counter == 0:
        print(NO_MORE_PLANTS_MESSAGE)

    if total_herbivores_counter == 0:
        print(NO_MORE_HERBIVORES_MESSAGE)

    if total_predators_counter == 0:
        print(NO_MORE_PREDATORS_MESSAGE)

def check_plant_number_exceeds_90_percents(curr_board):
    global total_plants_counter
    if 0.9 * (len(curr_board[0]) * len(curr_board)) <= total_plants_counter:
        print(PLANT_PERCENTAGE_EXCEEDS_90_PERCENTS)

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

    def check_if_life_span_ended(self, curr_board, location):
        self.life_span -= 1

        if self.life_span == 0:
            self.terminate_myself(curr_board, location)
            return True
        return False

    def terminate_myself(self, curr_board, location):
        kill_entity(curr_board, location)
        create_plant_in_new_position(curr_board, location)


class Plant (BasicEntity):
    def __init__(self, location):
        self.life_span = T_Plant
        self.location = location
        total_plants_counter += 1

    # a basic class for all instances in the program
    def update_iteration(self, curr_board, location):
        if self.terminate_myself(curr_board, location):
            total_plants_counter -= 1
        else:
            pass

class Herbivore(BasicEntity):
    def __init__(self, location):
        self.life_span = T_herbivore
        self.location = location
        total_herbivores_counter += 1

    # a basic class for all instances in the program
    def update_iteration(self, curr_board, location):
        if self.terminate_myself(curr_board, location):
            total_herbivores_counter -= 1
        else:
            pass




class Predator(BasicEntity):
    def __init__(self, location):
        self.life_span = T_predator
        self.location = location
        total_predators_counter += 1

    # a basic class for all instances in the program
    def update_iteration(self, curr_board, location):
        if self.terminate_myself(curr_board, location):
            total_predators_counter -= 1