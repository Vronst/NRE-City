"""Script for processig city data."""

import os
import sys

import nrecity as p


def main(path: str | None = None):
    """Main script for city data processing.

    Args:
        path (str): path to json file.

    Returns:
        None
    """
    path = os.getenv("DATA_PATH", "")
    manager = p.JsonManager(path + "miasta.json", name="cities")
    # data_manager = p.DataManager([manager])
    processor = p.CityProcessor(manager)

    processor.process_changes()


if __name__ == "__main__":
    import os

    path = str(os.getenv("DATA_PATH"))
    manager = p.DataManager()
    manager.create_manager(path + "events.json")
    manager.create_manager(path + "events_player.json")
    manager.create_manager(path + "event_frequency.json")
    manager.create_manager(path + "event_frequency_player.json")
    manager.create_manager(path + "curr_event.json")
    manager.create_manager(path + "curr_event_player.json")
    selector = p.EventSelector(manager)

    if len(sys.argv) == 1:
        main()
    elif "select" in sys.argv:
        print(selector.run())
    elif "event" in sys.argv:
        processor = p.EventProcessor()
        processor.event_chance = 100
        processor.run()
    else:
        json_manager = p.JsonManager(path + "miasta.json", "cities")
        rules_manager = p.JsonManager(path + "city_rules.json", "rules")
        manager([json_manager, rules_manager])
        manipulator = p.CommoditiesManipulator(manager)
        manipulator.reset_cities(141)
