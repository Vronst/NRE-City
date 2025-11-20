# noqa
import json
import os

from data_processor.city import City

PATH = os.getenv("CITY_PATH", "")
with open(PATH) as file:
    data = json.load(file)

fields = []
for name, value in data["after"][0].items():
    fields.append(name)


City1 = City(
    "City1",
    "big",
    ["mine", "port"],
    100,
    1,
    {
        "metal": {
            "quantity": 200,
            "price": 200,
            "regular_price": 150,
            "regular_quantity": 100,
        },
        "gems": {
            "quantity": 100,
            "price": 250,
            "regular_price": 300,
            "regular_quantity": 100,
        },
        "food": {
            "quantity": 150,
            "price": 60,
            "regular_price": 45,
            "regular_quantity": 100,
        },
        "fuel": {
            "quantity": 80,
            "price": 120,
            "regular_price": 80,
            "regular_quantity": 100,
        },
        "relics": {
            "quantity": 10,
            "price": 1300,
            "regular_price": 1300,
            "regular_quantity": 100,
        },
        "special": None,
    },
    0,
    [],
    ["City2"],
)

City2 = City(
    "City2",
    "small",
    [],
    1,
    1,
    {
        "metal": {
            "quantity": 20,
            "price": 20,
            "regular_price": 15,
            "regular_quantity": 10,
        },
        "gems": {
            "quantity": 10,
            "price": 20,
            "regular_price": 30,
            "regular_quantity": 10,
        },
        "food": {
            "quantity": 15,
            "price": 6,
            "regular_price": 4,
            "regular_quantity": 10,
        },
        "fuel": {
            "quantity": 8,
            "price": 12,
            "regular_price": 8,
            "regular_quantity": 10,
        },
        "relics": {
            "quantity": 1,
            "price": 100,
            "regular_price": 130,
            "regular_quantity": 10,
        },
        "special": None,
    },
    0,
    [],
    ["City2"],
)


class TestCity:  # noqa
    def test_compare(self):  # noqa
        assert City1.compare(City2) == {
            "food": {
                "price_diff": -54,
                "quantity_diff": -135,
                "reg_price": 45,
                "reg_quantity": 100,
            },
            "fuel": {
                "price_diff": -108,
                "quantity_diff": -72,
                "reg_price": 80,
                "reg_quantity": 100,
            },
            "gems": {
                "price_diff": -230,
                "quantity_diff": -90,
                "reg_price": 300,
                "reg_quantity": 100,
            },
            "metal": {
                "price_diff": -180,
                "quantity_diff": -180,
                "reg_price": 150,
                "reg_quantity": 100,
            },
            "relics": {
                "price_diff": -1200,
                "quantity_diff": -9,
                "reg_price": 1300,
                "reg_quantity": 100,
            },
        }
        assert City1.compare(City1) == {
            "food": {
                "price_diff": 0,
                "quantity_diff": 0,
                "reg_price": 45,
                "reg_quantity": 100,
            },
            "fuel": {
                "price_diff": 0,
                "quantity_diff": 0,
                "reg_price": 80,
                "reg_quantity": 100,
            },
            "gems": {
                "price_diff": 0,
                "quantity_diff": 0,
                "reg_price": 300,
                "reg_quantity": 100,
            },
            "metal": {
                "price_diff": 0,
                "quantity_diff": 0,
                "reg_price": 150,
                "reg_quantity": 100,
            },
            "relics": {
                "price_diff": 0,
                "quantity_diff": 0,
                "reg_price": 1300,
                "reg_quantity": 100,
            },
        }

    def test_fields(self):  # noqa
        for name in fields:
            City1.__getattribute__(name)
