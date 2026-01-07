from typing import Any

import matplotlib.pyplot as plt
import pandas as pd

from event_handling.observer import Observer
from lib_consts.board_consts import PRINT_DICT

class LiveObjectsObserver(Observer):
    """
    An object that in case of any events, prints the event to the console
    """
    def __init__(self):
        initial_entities = {key: 0 for key in PRINT_DICT.keys()}
        self.entities_per_iteration = {0: initial_entities}
        self.current_iteration = 0

    def finish_iter(self):
        self.current_iteration += 1
        self.entities_per_iteration[self.current_iteration] = \
            {key: 0 for key in PRINT_DICT.keys()}

    def on_event(self, dict_args: dict[str, Any]) -> None:
        """

        Args:
            event: a string indicating the event happening
        """

        type = dict_args["type"]
        factor = dict_args["factor"]
        if factor == "added":
            self.entities_per_iteration[self.current_iteration][type] += 1
        elif factor == "reduced":
            self.entities_per_iteration[self.current_iteration][type] -= 1

    def show_statistics_throughout_run(self):

        iterations = {'iteration': [iter for iter in self.entities_per_iteration.keys()]}
        categories = {}
        for type in PRINT_DICT.keys():
            categories[type.__name__] = []
        for iteration, values in self.entities_per_iteration.items():
            for type, amount in values.items():
                categories[type.__name__].append(amount)

        categories = {**iterations, **categories}
        df = pd.DataFrame(categories)
        ax = df.plot.bar(x='iteration', y=df.columns.drop(['iteration']), rot=0)
        ax.set_ylabel('iteration')
        ax.set_title('Amount of different entities per iteration')
        plt.show()
