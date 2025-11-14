"""City class to conviniently store city data."""

from dataclasses import asdict, dataclass, fields
from typing import Any

from .compare import commodieties_diff


@dataclass
class City:
    """Representation of city.

    Params:
        name (str): name of city.
        size (str): size of city.
        factory (list[str]): lists of factory located in city.
        fee (float): fee for entering.
        nr_of_conn (int): number of city connected to this.
        commodieties (dict[str, dict]): dictionary containing
            commodieties and their quantity, price and regular
            price.
        missions (int): number of missions.
        missions_titles (list[str]): list of missions titles.
        connections (list[str]): list of city names connected
            to this one.
    """

    name: str
    size: str
    factory: list[str]
    fee: float
    nr_of_conn: int
    commodities: dict[str, dict]
    missions: int
    missions_titles: list[str]
    connections: list[str]

    def compare(self, other: "City") -> dict:
        """Compares commodieties of cities.

        Returns:
            dict: Contains only fields that differ with
                the difference as value.
        """
        if not isinstance(other, self.__class__):
            raise TypeError("other object should be of type City")

        comparision = commodieties_diff(self.commodities, other.commodities)

        return comparision

    @classmethod
    def fields(cls) -> list[str]:
        """Fields of class."""
        return [field.name for field in fields(cls)]

    def to_dict(self) -> dict[str, Any]:
        """Changes this object into dict.

        Returns:
            dict(str, Any): dict with same fields as this class.
        """
        return asdict(self)
