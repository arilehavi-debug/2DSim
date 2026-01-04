from abc import ABC, abstractmethod

class Entity(ABC):
    life_span = 0
    location = ()

    @abstractmethod
    def update_life_span(self, new_life_span):
        pass

    @abstractmethod
    def update_location(self, new_location):
        pass

    @abstractmethod
    def update_iteration(self, curr_board, location):
            pass

    @abstractmethod
    def update_iteration(self, curr_board, location):
        pass



