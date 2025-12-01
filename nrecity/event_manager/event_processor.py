"""This file is responsible for loading and appling events."""

# FIXME: clean this code
import os
import random

from ..data_manager import DataManager, JsonManager
from .event_selector import EventSelector


class EventProcessor:
    """This class is responsible for loading and applying events."""

    event_chance: float = 10.0

    def __init__(self, reset: bool = False) -> None:
        """Init."""
        self.path: str | None = os.getenv("DATA_PATH")
        if not self.path:
            raise ValueError("DATA_PATH environment variable is not set")

        self.data_manager = DataManager()
        self.events_manager: JsonManager = self.data_manager.create_manager(
            self.path + "events.json"
        )
        # needs to be sure its for this specific save
        self.data_manager.create_manager(self.path + "curr_event.json")
        self.data_manager.create_manager(self.path + "event_frequency.json")
        # since cities can be edited in multiple places
        # there is no need to be sure the manager
        # is for this specific save
        self.city_manager = self.data_manager.get_manager(
            "miasta", self.path + "miasta.json"
        )
        self.cities = self.city_manager()
        self.selector = EventSelector(self.data_manager)

    def select_event(self) -> dict:
        """Uses EventSelector to select an event."""
        event: str = self.selector.run()

        return self.events_manager.data["events"][event]

    def __save_cities(self):
        """Save cities state before event."""
        # Just to make lsp not mark it xd
        assert isinstance(self.path, str)

        self.cities = self.city_manager()
        self.data_manager.get_manager(
            "pre_event_miasta", path=self.path + "pre_event_miasta.json"
        ).save(self.cities)

    def _alter_commodities(self, original: dict, alternation: dict) -> None:
        """Alters commodities according to specified alternation.

        Args:
            original (dict): Original commodities.
            alternation (dict): Changes to apply (add).
        """
        fields = ["quantity", "regular_quantity", "price", "regular_price"]
        for field in fields:
            if isinstance(original, dict):
                original[field] += alternation[field]

    # def __get_cities(self):
    #     cities = self.data_manager.get_manager("pre_event_miasta").data
    #     return cities

    def temporary_effects_manager(
        self, selected_event: dict | None, stop: bool = False
    ) -> None:
        """Manages temporary effects for the selected event.

        Args:
            selected_event (dict | None): The selected event.
            stop (bool): Whether to stop the effects.
        """
        if stop:
            cities = self.data_manager.get_manager("pre_event_miasta").data
            self.city_manager.save(cities)
            return

        if selected_event is None:
            return

        if selected_event["type"] == "temporary":
            self.__save_cities()

    def _process_event(self) -> None:
        """Process the current event."""
        selected_event: dict = self.select_event()

        if selected_event["target"] != "city":
            return

        self.temporary_effects_manager(selected_event)
        effect = selected_event["effects"]["commodities"]

        # FIXME: If event ever target certain city it should be changed
        for city in self.cities["cities"]:
            for commodity, stats in city["commodities"].items():
                self._alter_commodities(stats, effect[commodity])

        self.cities["after"] = self.cities["cities"]
        self.city_manager.save(self.cities)
        print(self.cities["cities"][0]["commodities"])

        # TODO: add other mods

    def __set_event_to_none(self):
        manager = self.data_manager.get_manager("curr_event")
        manager.save({"event_id": None})

    def run(self):
        """Run the event processor."""
        if random.randint(1, 100) > self.event_chance:
            self.__set_event_to_none()
            return

        self._process_event()

    def stop(self):
        """Restores state before events and removes events."""
        self.temporary_effects_manager(None, stop=True)
        self.__set_event_to_none()
