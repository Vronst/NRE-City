"""This file is responsible for selecting events."""

import random

from nrecity.data_manager.json_manager import JsonManager

from ..data_manager import DataManager


class EventSelector:
    """This class is responsible for selecting events.

    It excludes events when their repetition is too frequent.

    It also excludes events that are too close in time to each other.
    """

    def __init__(  # noqa
        self,
        event_file_menager: DataManager,
        reset: bool = False,
    ) -> None:
        """Init.

        Args:
            data_manager (DataManager): The data manager containing
                'events' and 'curr_event'.
            reset (bool): Whether to reset the event selector.
        """
        if reset:
            self.reset()
        self.event_file_menager = event_file_menager
        self.__get_managers()

        self._load()

    def __get_manager(self, name: str) -> JsonManager:
        manager = self.event_file_menager.get_manager(name, name + ".json")
        return manager

    def __get_managers(self):
        name: str = "event_frequency"
        self.frequency_manager = self.__get_manager(name)

        name = "events"
        self.event_manager = self.__get_manager(name)

        name = "curr_event"
        self.curr_event_manager = self.__get_manager(name)

    def _load_frequency(self):
        self.frequency = self.frequency_manager.data["events"]
        if len(self.frequency) == len(self.events):
            return

        for event in self.events:
            self.frequency[event["id"]] = 1

    def __load_events(self):
        self.events = self.event_manager.data["events"]

    def _load(self):
        self.__load_events()
        self._load_frequency()

    def reset(self):
        """Reset the event selector.

        Selector will forget about events that occured.
        """
        for event in self.events:
            self.frequency[event["id"]] = 1

        self.frequency_manager.save({"events": self.frequency})

    def run(self) -> dict:
        """Run the event selector.

        Selector will select events that are not too
        frequent and not too close in time to each other.

        Returns:
            dict: The selected event.
        """
        weights = [1 / x for x in self.frequency.values()]
        events = list(self.frequency.keys())
        selected_event: dict = random.choices(events, weights=weights, k=1)[0]

        self.curr_event_manager.save({"event_id": selected_event})

        self.frequency[selected_event] += 1
        self.frequency_manager.save({"events": self.frequency})

        return selected_event
