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

    if len(sys.argv) == 1:
        main()
    elif "event" in sys.argv:
        manager = p.DataManager()
        manager.create_manager(path + "events.json")
        manager.create_manager(path + "event_frequency.json")
        manager.create_manager(path + "curr_event.json")
        selector = p.EventSelector(manager)
        print(selector.run())
    else:
        json_manager = p.JsonManager(path + "miasta.json", "cities")
        rules_manager = p.JsonManager(path + "city_rules.json", "rules")
        data_manager = p.DataManager([json_manager, rules_manager])
        manipulator = p.CommoditiesManipulator(data_manager)
        manipulator.reset_cities(141)
