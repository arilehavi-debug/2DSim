from typing import Any

import matplotlib.pyplot as plt
import pandas as pd

from event_handling.event_manager import EventManager
from event_handling.observer import Observer
from lib_consts.board_consts import PRINT_DICT

class LiveObjectsObserver(Observer):
    """
    An object that counts the
    amount of live entities per iteration.
    """
    def __init__(self, mngr: EventManager):
        mngr.subscribe(self, [("entity added",
                               LiveObjectsObserver.on_event),
                               ("iteration ended",
                                LiveObjectsObserver.finish_iter),
                               ("game finished",
                                LiveObjectsObserver.show_statistics_throughout_run)])
        initial_entities = dict.fromkeys(PRINT_DICT, 0)
        self.entities_per_iteration = {0: initial_entities}
        self.current_iteration = 0

    def finish_iter(self):
        """
        Updating the current iteration.
        Adding new dictionary to count entities in the next round.
        """
        self.current_iteration += 1
        self.entities_per_iteration[self.current_iteration] = dict.fromkeys(PRINT_DICT, 0)

    def on_event(self, dict_args: dict[str, Any]) -> None:
        """
        Updates the counter when another entity created.
        Args:
            dict_args: dictionary containing what kind of entity added.
        """

        self.entities_per_iteration[self.current_iteration][dict_args["type"]] += 1

    def show_statistics_throughout_run(self):
        """
        plotting the number of live entities per iteration.
        """
        iterations = {'iteration': list(self.entities_per_iteration.keys())}
        categories = {class_type.__name__: [] for class_type in PRINT_DICT}

        for values in self.entities_per_iteration.values():
            for class_type, amount in values.items():
                categories[class_type.__name__].append(amount)

        categories = {**iterations, **categories}
        df = pd.DataFrame(categories)
        ax = df.plot.bar(x='iteration', y=df.columns.drop(['iteration']), rot=0)
        ax.set_ylabel('iteration')
        ax.set_title('Amount of different entities per iteration')
        plt.show()
