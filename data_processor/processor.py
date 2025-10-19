"""This module contains class responsible for processing city data."""

import random
from typing import Any

from .city import City
from .compare import commodieties_diff
from .loader import DataLoader


class CityProcessor:
    """Processes city data and players actions."""

    def __init__(self, loader: DataLoader) -> None:
        """Init.

        Args:
            loader (DataLoader): loader responsible for
                handing data to this class.

        Returns:
            None.
        """
        self.loader = loader
        # self.events = loader.events()

    def get_dict_of_cities(self, state: str = "after") -> dict[str, City]:
        """Creates list of objects of City.

        These objects represents cities before/after players and AIs
        actions were taken.

        Returns:
            list[City]: list containing City objects.
        """
        requested: list = (
            self.loader.cities_after
            if state == "after"
            else self.loader.cities_before
        )
        city_dict: dict[str, City] = {}
        for city in requested:
            new_city = {}
            for field in City.fields():
                new_city[field] = city[field]
            city_dict[city["name"]] = City(**new_city)
            # city_list.append(City(**city))

        return city_dict

    def get_comparison(self) -> dict[str, Any]:
        """Compares cities data before and after.

        Returns:
            dict[str, Any]: Dict with changes.
        """
        before: dict = self.get_dict_of_cities("before")
        after: dict = self.get_dict_of_cities()

        result: dict = {}

        for name, city in before.items():
            result[name] = commodieties_diff(
                city.commodities, after[name].commodities
            )

        return result

    def process_changes(self):
        """Processes city data.

        Processes data of city and changes made by players,
        and saves them in json as cities.

        Returns:
            None
        """
        self.cities = self.get_dict_of_cities()
        self.diff = self.get_comparison()
        fee_add = self._process_commodieties()
        self._process_fee(fee_add)
        self._process_contracts()
        self.__save_changes()

    def __save_changes(self):
        print(self.cities)

    def _process_commodieties(self) -> None:
        increase: int = 0

        for name, commodieties in self.diff.items():
            for item_type, data in commodieties.items():
                quantity = data["quantity_diff"]
                city_comm = self.cities[name].commodities[item_type]

                self.__proces_quantity(city_comm, quantity)

                change: int = round(
                    self.__process_price(city_comm, quantity), 0
                )

                increase += change

    def __proces_quantity(self, city_comm, quantity):
        if quantity == 0:
            return

        reg_quant = city_comm["regular_quantity"]

        # changes should occur only when change
        # in quanityt is signifacant
        if abs((reg_quant - quantity) / reg_quant) < 0.5:
            return

        # leaving up to chance posibility of changing standard
        # quality to limit player influence
        city_comm["regular_quantity"] = random.choice(
            (reg_quant, reg_quant * random.uniform(1.25, 1.5))
        )
        city_comm["quantity"] = city_comm["regular_quantity"]

    def __process_price(self, city_comm, quantity):
        reg_price = city_comm["regular_price"]

        dif_price = reg_price * random.uniform(0.5, 0.10)
        if quantity <= 0:
            dif_price *= -1
        city_comm["regular_price"] = random.choice(
            (reg_price, reg_price + dif_price)
        )

        # to spice things up, sometimes instead of change of price
        # it will be just temporary discount
        reg_price = city_comm["regular_price"]
        price = city_comm["price"]
        city_comm["price"] = random.choice(
            (reg_price, price + (dif_price * price * 1.3))
        )

        return dif_price

    def _process_fee(self, fee_add):
        pass

    def _process_contracts(self):
        pass
