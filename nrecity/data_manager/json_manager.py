"""This module contains class for loading and saving data to json."""

import json


class JsonManager:
    """Loads and saves data from to json file."""

    def __init__(self, path: str, name: str | None = None) -> None:
        """Initialize DataLoader.

        Args:
            path (str): path to json file (for saving and loading).
            name (str | None): name of the data manager, default None.

        Returns:
            None
        """
        self.name = name
        self.__path = path
        self()

    def __call__(self) -> dict:
        """Load data with DataLoader.

        Uses path from initialization if not provided.

        """
        return self.__load()

    def __load(self) -> dict:
        with open(self.__path) as file:
            self.__data = json.load(file)
        return self.__data

    def save(self, data: dict) -> None:
        """Saves data to json file.

        Args:
            data (dict): dict with cities data.

        Returns:
            None
        """
        with open(self.__path, "w") as file:
            json.dump(data, file, indent=2)

    @property
    def path(self) -> str:
        """Returns path to json file.

        Returns:
            str: path to json file.
        """
        return self.__path

    @path.setter
    def path(self, value: str) -> None:
        raise KeyError("Path cannot be changed")

    @property
    def data(self) -> dict:
        """Returns data from json file."""
        return self.__data

    @data.setter
    def data(self, value: dict) -> None:
        # FIXME: not sure what i want xd
        self.__data = value
