from abc import ABC, abstractmethod
from typing import Any

class Observer(ABC):
    """
    Abstract class implementing an interface for an
    observer of an event
    """

    @abstractmethod
    def on_event(self, dict_args: dict[str, Any]) -> None:
        """
        An abstract function that determines what to do in case of an event
        Args:
            event: a function to call in case of an event
        """
    pass

    @abstractmethod
    def on_event(self) -> None:
        """
        An abstract function that determines what to do in case of an event
        Args:
            event: a function to call in case of an event
        """
    pass

    @abstractmethod
    def show_statistics_throughout_run(self):
        """
        An abstract function that determines what to do in case of an event
        """
    pass
