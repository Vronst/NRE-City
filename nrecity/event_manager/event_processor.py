"""This file is responsible for loading and appling events."""

import os

from ..data_manager import DataManager
from .event_selector import EventSelector


class EventProcessor:
    """This class is responsible for loading and applying events."""

    def __init__(self, reset: bool = False) -> None:
        """Init."""
        path: str | None = os.getenv("DATA_PATH")
        if not path:
            raise ValueError("DATA_PATH environment variable is not set")

        data_manager = DataManager()
        data_manager.create_manager(path + "events.json")
        data_manager.create_manager(path + "curr_event.json")
        data_manager.create_manager(path + "event_frequency.json")
        self.selector = EventSelector(data_manager)
