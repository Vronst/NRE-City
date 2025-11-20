"""Module for manipulating commodity data."""

import random

from ..data_processor import JsonManager, factory


class CommoditiesManipulator:
    """Class for manipulating commodity data."""

    rules_map: dict = {
        "fee": "fee_range",
        "factory": "factory_range",
        "commodities": "commodities",
    }

    def __init__(
        self, json_manager: JsonManager, rules_manager: JsonManager
    ) -> None:
        """Saves json_manager with its paths.

        Args:
            json_manager (JsonManager): The JSON manager for commodity data.
            rules_manager (JsonManager): The JSON manager for rules.
        """
        self.json_manager = json_manager
        self.rules = rules_manager()
        self._load_data()

    def _load_data(self):
        self.all_data = self.json_manager()
        self.data = self.all_data["cities"]

    def _save_data(self):
        self.json_manager.save(self.all_data)

    def reset_cities(self, seed: int | None = None):
        """Sets (if no seed) random within rules data for cities.

        Args:
            seed (int | None): The seed for random number generation.
                Default is None.
        """
        if seed is not None:
            random.seed(seed)

        for city in self.data:
            rules = self.rules[city["size"]]
            for field in self.rules_map:
                range_from_rules = rules[self.rules_map[field]]
                match field:
                    case "factory":
                        factories: set = set()
                        for _ in range(*range_from_rules):
                            factories.add(
                                random.choice(list(factory.values()))
                            )
                        city[field] = list(factories)
                    case "commodities":
                        # TODO: Check if its better to have reg and normal same
                        for commodity in city[field]:
                            if commodity == "special":
                                continue

                            comm_range = rules["commodities"][commodity]
                            city[field][commodity]["price"] = random.randint(
                                *comm_range["price_range"]
                            )
                            city[field][commodity]["regular_price"] = (
                                random.randint(*comm_range["price_range"])
                            )
                            city[field][commodity]["quantity"] = (
                                random.randint(*comm_range["quantity_range"])
                            )
                            city[field][commodity]["regular_quantity"] = (
                                random.randint(*comm_range["quantity_range"])
                            )
                    case _:
                        city[field] = random.randint(*range_from_rules)
                        continue
        self.all_data["after"] = self.data
        self.all_data["cities"] = self.data
        self._save_data()
