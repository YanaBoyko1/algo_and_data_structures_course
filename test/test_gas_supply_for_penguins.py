import unittest
from src.supply_gas_for_penguins import gas_supply


class TestGasSupply(unittest.TestCase):
    def test_gas_supply(self):
        list_city = ["Lviv", "Kyiv", "Odessa", "Kharkiv"]
        list_storage = ["Storage_1", "Storage_2", "Storage_3"]
        list_active_gas_pipelines = [
            ["Lviv", "Kyiv"],
            ["Kyiv", "Odessa"],
            ["Storage_1", "Lviv"],
            ["Storage_2", "Odessa"],
        ]

        unreachable_cities = gas_supply(
            list_city, list_storage, list_active_gas_pipelines
        )

        expected_unreachable_cities = {
            "Storage_1": ["Kharkiv"],
            "Storage_2": ["Lviv", "Kyiv", "Kharkiv"],
            "Storage_3": ["Lviv", "Kyiv", "Odessa", "Kharkiv"],
        }
        self.assertEqual(unreachable_cities, expected_unreachable_cities)

    def test_gas_supply_no_unreachable_cities(self):
        list_city = ["Lviv", "Kyiv", "Odessa", "Kharkiv"]
        list_storage = ["Storage_1", "Storage_2", "Storage_3"]
        list_active_gas_pipelines = [
            ["Lviv", "Kyiv"],
            ["Kyiv", "Odessa"],
            ["Storage_1", "Lviv"],
            ["Storage_2", "Odessa"],
            ["Storage_3", "Kyiv"],
        ]

        unreachable_cities = gas_supply(
            list_city, list_storage, list_active_gas_pipelines
        )

        expected_unreachable_cities = {
            "Storage_1": ["Kharkiv"],
            "Storage_2": ["Lviv", "Kyiv", "Kharkiv"],
            "Storage_3": ["Lviv", "Kharkiv"],
        }
        self.assertEqual(unreachable_cities, expected_unreachable_cities)

    def test_gas_supply_no_storages(self):
        list_city = ["Lviv", "Kyiv", "Odessa", "Kharkiv"]
        list_storage = []
        list_active_gas_pipelines = [
            ["Lviv", "Kyiv"],
            ["Kyiv", "Odessa"],
        ]

        unreachable_cities = gas_supply(
            list_city, list_storage, list_active_gas_pipelines
        )

        expected_unreachable_cities = {}
        self.assertEqual(unreachable_cities, expected_unreachable_cities)


if __name__ == "__main__":
    unittest.main()
