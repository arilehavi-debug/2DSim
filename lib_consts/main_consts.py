from event_handling.console_observer import ConsoleObserver
from event_handling.entity_killing_observer import EntityKillingObserver
from event_handling.herbivore_reproduction_observer import HerbivoreReproductionObserver
from event_handling.live_objects_observer import LiveObjectsObserver

OBSERVER_TYPES_TO_INIT = [ConsoleObserver, EntityKillingObserver,
                          HerbivoreReproductionObserver, LiveObjectsObserver]
