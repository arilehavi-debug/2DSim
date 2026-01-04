import MobileEntity

class Herbivore(MobileEntity):
    R_herbivore_sight = 3
    T_cooldown = 3

    def __init__(self, location, life_span):
        self.life_span = life_span
        self.location = location

    def update_life_span(self, new_life_span):
        self.life_span = new_life_span

    def update_location(self, new_location):
        self.location = new_location

    # a basic class for all instances in the program
    def update_iteration(self, curr_board, location):
        self.life_span -= 1
        # check the closest
