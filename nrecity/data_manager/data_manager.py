"""This module contains the DataManager class."""

from .json_manager import JsonManager


class DataManager:
    """Manages multiples json.

    Allows to access multiple JsonManagers.

    Args:
        json_managers (dict[JsonManager]): The json managers to manage.
    """

    def __init__(self, json_managers: list[JsonManager]) -> None:
        """Init."""
        self.json_managers = {}
        for manager in json_managers:
            self.add_manager(manager)

    def add_manager(self, manager: JsonManager):
        """Adds a new JsonManager to the list.

        Args:
            manager (JsonManager): The JsonManager to add.
        """
        if manager.name:
            self.json_managers[manager.name] = manager
        else:
            name = manager.path.split("/")[-1]
            self.json_managers[name] = manager

    def get_manager(
        self, name_of_manager: str, path: str | None = None
    ) -> JsonManager:
        """Returns the JsonManager with the given name.

        Args:
            name_of_manager (str): The name of the JsonManager to return.
            path (str): In case no JsonManagers are found, and the
                path is specified, new JsonManager with that path
                will be created.

        Returns:
            JsonManager: The JsonManager with the given name.
        """
        if name_of_manager in self.json_managers:
            return self.json_managers[name_of_manager]
        elif path:
            return self.create_manager(name_of_manager)
        else:
            raise ValueError(
                "No JsonManager found with name '{name_of_manager}'"
            )

    def create_manager(
        self, path: str, name: str | None = None
    ) -> JsonManager:
        """Creates a new JsonManager with the given path.

        Args:
            path (str): The path of the JsonManager to create.
            name (str | None): The name of the JsonManager to create.
                If None, the name will be the last part of the path.

        Returns:
            JsonManager: The JsonManager with the given path.
        """
        manager: JsonManager = JsonManager(path)
        self.add_manager(manager)
        return manager
