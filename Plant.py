import MobileEntity

class Plant (MobileEntity):
    def __init__(self, location):
        self.life_span = self.const_dict["T_Plant"]
        self.location = location

    # a basic class for all instances in the program
    def update_iteration(self, curr_board, location):
        self.life_span -= 1
        # in case it's time for the plant to terminate itself
        if self.life_span == 0:
            self.kill_entity(curr_board, location)
            create_new_entity(curr_board, location)