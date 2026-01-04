from numpy.f2py.auxfuncs import throw_error

from code_from_previous_branches.entities import BasicEntity
import yaml
import Entity

class MobileEntity(Entity):
    life_span = 0
    location = ()
    const_dict = {}

    def __init__(self, location, life_span):
        self.life_span = life_span
        self.location = location

    def update_life_span(self, new_life_span):
        self.life_span = new_life_span

    def update_location(self, new_location):
        self.location = new_location

    def parse_config_file(self, config_file_name):
        try:
            with open(f'{config_file_name}.yaml', 'r') as f:
                self.const_dict = yaml.safe_load(f)

        except FileNotFoundError:
            throw_error(FileNotFoundError)

    def update_iteration(self, curr_board, location):
        pass