import logging

from event_handling.observer import Observer

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

class EventManager:
    """
    Class of event manager - in charge of managing events
    throughout the runtime of the game
    """
    def __init__(self):
        """
        Constructor for class "EventManager"
        """
        self._observers = []

    def subscribe(self, observer: Observer) -> None:
        """
        function to allow subscribing for an event happening
        Args:
         observer: object wanting to subscribe for a certain event
        :return:
        """
        self._observers.append(observer)
        logging.info("Observer subscribed")

    def notify(self, event: str) -> None:
        """
        notifying to all subscribers over an event happening
        Args:
            event: a string informing an event happening on screen
        """
        for observer in self._observers:
            observer.on_event(event)
