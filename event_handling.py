import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

class Observer(ABC):
    @abstractmethod
    def on_event(self, event):
        pass

class ConsoleObserver(Observer):
    def on_event(self, event):
        print(f"Observer received event: {event}")

class EventManager:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer: Observer):
        self._observers.append(observer)
        logging.info("Observer subscribed")

    def notify(self, event):
        for observer in self._observers:
            observer.on_event(event)
