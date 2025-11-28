"""This file is responsible for loading and appling events."""

import os

from ..data_processor import JsonManager
from . import EventSelector


class EventProcessor:
    """This class is responsible for loading and applying events."""

    def __init__(self, reset: bool = False) -> None:
        """Init."""
        path: str | None = os.getenv("DATA_PATH")
        if not path:
            raise ValueError("DATA_PATH environment variable is not set")

        self.json_manager = JsonManager(path + "events.json")
        self.selector = EventSelector(reset)
