from event_handling.observer import Observer

class ConsoleObserver(Observer):
    """
    An object that in case of any events, prints the event to the console
    """
    def on_event(self, event: dict[str, str]) -> None:
        """
        Printing the event occuring to the screen
        :Args:
            event: a string insicating the event happening
        """
        event = event["data"]
        print(f"Observer received event: {event}")

    def on_evemt(self) -> None:
        return

    def show_statistics_throughout_run(self):
        pass