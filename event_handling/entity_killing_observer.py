from typing import Any

import matplotlib.pyplot as plt
import pandas as pd

from event_handling.event_manager import EventManager
from event_handling.observer import Observer
from lib_consts.board_consts import PRINT_DICT


class EntityKillingObserver(Observer):
    """
    An observer object for counting
    the entities killed per iteration.
    """

    def __init__(self, mngr: EventManager):
        """
        Constructor for the ConsoleObserver.object.
        Args:
             mngr: the game's event manager
        """
        mngr.subscribe(self, [("entity reduced",
                               EntityKillingObserver.on_event),
                              ("iteration ended",
                               EntityKillingObserver.finish_iter),
                              ("game finished",
                               EntityKillingObserver.show_statistics_throughout_run)])
        initial_entities = dict.fromkeys(PRINT_DICT, 0)
        self.entities_per_iteration = {0: initial_entities}
        self.current_iteration = 0

    def finish_iter(self):
        """
        Updating the class's variables every game iteration.
        """
        self.current_iteration += 1
        self.entities_per_iteration[self.current_iteration] = dict.fromkeys(PRINT_DICT, 0)

    def on_event(self, dict_args: dict[str, Any]) -> None:
        """
        Function adding a killing that happened throughout the game.
        Args:
            dict_args: type to add as killed once
        """
        self.entities_per_iteration[self.current_iteration][dict_args["type"]] += 1

    def show_statistics_throughout_run(self):
        """
        Function drawing the killings that happened
        throughout the game per iteration.
        """
        iterations = {'iteration': list(self.entities_per_iteration.keys())[1:]}
        categories = {class_type.__name__: [] for class_type in PRINT_DICT.keys()}
        for iteration, values in self.entities_per_iteration.items():
            for class_type, amount in values.items():
                if iteration > 0:
                    categories[class_type.__name__].append(amount)

        categories = {**iterations, **categories}
        df = pd.DataFrame(categories)
        ax = df.plot.bar(x='iteration', y=df.columns.drop(['iteration']), rot=0)
        ax.set_ylabel('iteration')
        ax.set_title('Amount of different entities killed per iteration')
        plt.show()
