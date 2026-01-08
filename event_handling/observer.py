from abc import ABC, abstractmethod
from typing import Any


class Observer(ABC):
    """
    Abstract class implementing an interface for an
    observer of an event.
    """

    @abstractmethod
    def on_event(self, dict_args: dict[str, Any]) -> None:
        """
        An abstract function that determines what to do in case of an event
        Args:
            dict_args: a dictionary holding the necessary parameters for the function
        """

    @abstractmethod
    def show_statistics_throughout_run(self):
        """
        An abstract function that determines what to do in case of an event
        """
