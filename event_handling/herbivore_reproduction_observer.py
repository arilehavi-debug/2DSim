from typing import Any

import matplotlib.pyplot as plt

from event_handling.observer import Observer
from event_handling.event_manager import EventManager


class HerbivoreReproductionObserver(Observer):
    """
    An object that in case of any events,
    prints the event to the console.
    """

    def __init__(self, mngr: EventManager):
        self.reproduction_counter = {1: 0}
        self.current_iteration = 0
        mngr.subscribe(self, [("herbivore reproduction",
                               HerbivoreReproductionObserver.on_event),
                              ("iteration ended",
                               HerbivoreReproductionObserver.finish_iter),
                              ("game finished",
                               HerbivoreReproductionObserver.show_statistics_throughout_run)])

    def finish_iter(self):
        """
        Updating the current iteration to number
        the herbivores' reproduction.
        """
        self.current_iteration += 1
        self.reproduction_counter[self.current_iteration] = 0

    def on_event(self, dict_args: dict[str, Any]) -> None:
        """
        Function to add an instance
        of herbivores' reproduction.
        Args:
            dict_args: a string indicating that the event happened
        """
        self.reproduction_counter[self.current_iteration] += 1

    def show_statistics_throughout_run(self):
        """
        Function to draw the number of reproductions
        per iteration.
        """
        plt.plot(list(self.reproduction_counter.keys()),
                 list(self.reproduction_counter.values()))
        plt.xlabel('iteration')
        plt.ylabel('herbivore reproductions')
        plt.title('Amount of herbivore reproductions per iteration')
        plt.show()
