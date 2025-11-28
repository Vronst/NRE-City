"""This file is responsible for selecting events."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..data_manager import DataManager


class EventSelector:
    """This class is responsible for selecting events.

    It excludes events when their repetition is too frequent.

    It also excludes events that are too close in time to each other.
    """

    def __init__(  # noqa
        self,
        event_file_menager: DataManager,
        frequency_file_manager: DataManager,
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
        self._load()

    def _load(self):
        pass

    def reset(self):
        """Reset the event selector.

        Selector will forget about events that occured.
        """
        pass

    def run(self):
        """Run the event selector.

        Selector will select events that are not too
        frequent and not too close in time to each other.
        """
        pass
