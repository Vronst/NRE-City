"""Script for processig city data."""

import os
import sys

import data_processor as p


def main(path: str | None = None):
    """Main script for city data processing.

    Args:
        path (str): path to json file.

    Returns:
        None
    """
    # loader = p.JsonManager("data.json")
    path = os.getenv('CITY_PATH', None)
    manager = p.JsonManager(path)
    processor = p.CityProcessor(manager)

    processor.process_changes()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        main(path)
    else:
        main()
