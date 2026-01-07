import logging
from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def on_event(self, event):
        pass