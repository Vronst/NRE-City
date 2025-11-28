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
    if "reset" not in sys.argv:
        main()
    else:
        import os

        path = str(os.getenv("DATA_PATH"))
        json_manager = p.JsonManager(path + "miasta.json", "cities")
        rules_manager = p.JsonManager(path + "city_rules.json", "rules")
        data_manager = p.DataManager([json_manager, rules_manager])
        manipulator = p.CommoditiesManipulator(data_manager)
        manipulator.reset_cities(141)
