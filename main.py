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
    # loader = p.JsonManager("data.json")
    path = os.getenv("CITY_PATH", "")
    manager = p.JsonManager(path)
    processor = p.CityProcessor(manager)

    processor.process_changes()


if __name__ == "__main__":
    if "reset" not in sys.argv:
        main()
    else:
        import os

        path = str(os.getenv("CITY_PATH"))
        rules = str(os.getenv("CITY_RULES"))
        json_manager = p.JsonManager(path)
        rules_manager = p.JsonManager(rules)
        manipulator = p.CommoditiesManipulator(json_manager, rules_manager)
        manipulator.reset_cities(141)
