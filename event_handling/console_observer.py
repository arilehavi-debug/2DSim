from event_handling.observer import Observer

class ConsoleObserver(Observer):
    """
    An object that in case of any events, prints the event to the console
    """
    def on_event(self, event: str) -> None:
        """
        Printing the event occuring to the screen
        :Args:
            event: a string insicating the event happening
        """
        print(f"Observer received event: {event}")