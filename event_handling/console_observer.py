from typing import Any

from event_handling.event_manager import EventManager
from event_handling.observer import Observer

class ConsoleObserver(Observer):
    """
    An object that in case of any events, prints the event to the console.
    """
    def __init__(self, mngr: EventManager):
        """
        Constructor for the ConsoleObserver.object.
        param
            mngr: event manager to subscribe to
        """
        mngr.subscribe(self, [("no more entities left",
                               ConsoleObserver.on_event),
                               ("plant percentage exceeds 90 percent",
                                ConsoleObserver.on_event)])

    def on_event(self, dict_args: dict[str, Any]) -> None:
        """
        Printing the event happening to the screen.
        :Args:
            event: a string indicating the event happening
        """
        print(f"Observer received event: {dict_args["data"]}")

    def show_statistics_throughout_run(self):
        """
        A function responsible for orchestrating an action
        in the end of the run.
        In this instance, it's not relevant.
        """
