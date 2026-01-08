import logging
from typing import Callable, Any

from event_handling.observer import Observer

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


class EventManager:
    """
    Class of event manager - in charge of managing events
    throughout the runtime of the game.
    """

    def __init__(self):
        """
        Constructor for class "EventManager".
        """
        self._observers = {}

    def subscribe(self, observer: Observer, event_types: list[(str, Callable)]) -> None:
        """
        Function to allow subscribing for an event happening.
        Args:
            observer: object wanting to subscribe for a certain event
            event_types: list of event types snd function to call in case of an event
        """
        for (event, func) in event_types:
            if event in self._observers.keys():
                self._observers[event].append((observer, func))
            else:
                self._observers[event] = [(observer, func)]
        logging.info("Observer subscribed")

    def notify(self, event: str, **kwargs: dict[str, Any]) -> None:
        """
        Notifying to all subscribers over an event happening.
        Args:
            event: a string informing an event happening on screen
        """
        for (observer, function) in self._observers[event]:
            if len(kwargs) > 0:
                function(observer, kwargs)
            else:
                function(observer)
