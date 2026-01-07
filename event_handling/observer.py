from abc import ABC, abstractmethod
from typing import Callable

class Observer(ABC):
    """
    Abstract class implementing an interface for an
    observer of an event
    """

    @abstractmethod
    def on_event(self, event: Callable) -> None:
        """
        An abstract function that determines what to do in case of an event
        Args:
            event: a function to call in case of an event
        """
        pass
