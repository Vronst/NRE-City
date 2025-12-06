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
        menagers: DataManager,
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
        self.menagers = menagers
        self.__get_managers()

        self._load()

    def __get_manager(self, name: str) -> JsonManager:
        manager = self.menagers.get_manager(name, name + ".json")
        return manager

    def __get_managers(self):
        name: str = "event_frequency"
        self.frequency_manager = self.__get_manager(name)

        name = "event_frequency_player"
        self.frequency_player_manager = self.__get_manager(name)

        name = "events"
        self.event_manager = self.__get_manager(name)

        name = "curr_event"
        self.curr_event_manager = self.__get_manager(name)

        name = "curr_event_player"
        self.curr_event_player_manager = self.__get_manager(name)

        name = "events_player"
        self.player_event_manager = self.__get_manager(name)

    def _load_frequency(self):
        self.city_event_frequency = self.frequency_manager.data["events"]
        self.player_event_frequency = self.frequency_player_manager.data[
            "events"
        ]
        self.__set_frequency("city")
        self.__set_frequency("player")

    def __set_frequency(self, target: str = "city"):
        # FIXME: could be done better
        if target == "city":
            curr_frequency = self.city_event_frequency
            event_list = self.events
        elif target == "player":
            curr_frequency = self.player_event_frequency
            event_list = self.p_events
        else:
            return

        if len(curr_frequency) != len(event_list):
            for event in event_list:
                if target == "city":
                    # self.city_event_frequency[event["id"]] = 1
                    self.city_event_frequency[event] = 1
                if target == "player":
                    # self.player_event_frequency[event["id"]] = 1
                    self.player_event_frequency[event] = 1

    def __load_events(self):
        self.events = self.event_manager.data["events"]
        self.p_events = self.player_event_manager.data["events"]

    def _load(self):
        self.__load_events()
        self._load_frequency()

    def reset(self, target: str = "all"):
        """Reset the event selector.

        Selector will forget about events that occured.

        Args:
            target (str): The target to reset. Can be "city", "player",
                or "all".
        """
        match target:
            case "city":
                self.__reset("city")
            case "player":
                self.__reset("player")
            case "all":
                self.__reset("city")
                self.__reset("player")

    def __reset(self, target: str = "city") -> None:
        events = self.p_events if target != "city" else self.events
        frequency = (
            self.player_event_frequency
            if target == "city"
            else self.city_event_frequency
        )

        for event in events:
            frequency[event["id"]] = 1

        self.frequency_manager.save({"events": self.city_event_frequency})

    def run(self, city: bool = True, player: bool = True) -> dict:
        """Run the event selector.

        Selector will select events that are not too
        frequent and not too close in time to each other.

        Args:
            city (bool): Whether to consider city events.
            player (bool): Whether to consider player events.

        Returns:
            dict: The selected event.
        """
        city_event = player_event = None

        if city:
            city_event = self._process_event("city")
        if player:
            player_event = self._process_event("player")

        return {"city_event": city_event, "player_event": player_event}

    def _process_event(self, target: str = "city") -> str:
        if target == "city":
            frequency = self.city_event_frequency
            manager = self.curr_event_manager
            event_manager = self.frequency_manager
        elif target == "player":
            frequency = self.player_event_frequency
            manager = self.curr_event_player_manager
            event_manager = self.frequency_player_manager
        else:
            raise ValueError("Invalid target - use 'player' or 'city'")

        weights = [1 / x for x in frequency.values()]
        events = list(frequency.keys())
        selected_event: str = random.choices(events, weights=weights, k=1)[0]

        manager.save({"event_id": selected_event})

        frequency[selected_event] += 1

        event_manager.save({"events": frequency})

        return selected_event
