"""This file is responsible for loading and appling events."""

import os

from ..data_manager import DataManager, JsonManager
from .event_selector import EventSelector


class EventProcessor:
    """This class is responsible for loading and applying events."""

    def __init__(self, reset: bool = False) -> None:
        """Init."""
        path: str | None = os.getenv("DATA_PATH")
        if not path:
            raise ValueError("DATA_PATH environment variable is not set")

        data_manager = DataManager()
        self.events: JsonManager = data_manager.create_manager(
            path + "events.json"
        )
        data_manager.create_manager(path + "curr_event.json")
        data_manager.create_manager(path + "event_frequency.json")
        self.city_manager = data_manager.get_manager(path + "miasta.json")
        self.selector = EventSelector(data_manager)

    def process_event(self) -> None:
        """Process the current event."""
        # TODO: decide on implementation
        event: str = self.selector.run()["event_id"]
        selected_event = self.events.data[event]
