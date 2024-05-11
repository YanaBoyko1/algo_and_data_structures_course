from unittest import TestCase, main
from src.supply_gas_for_penguins import gas_supply


class TestGasSupply(TestCase):
    def test_gas_supply(self):
        list_city = ['Lviv', 'Kyiv', 'Odessa', 'Kharkiv']
        list_storage = ['Storage_1', 'Storage_2', 'Storage_3']
        list_active_gas_pipelines = [['Lviv', 'Kyiv'], ['Kyiv', 'Odessa'], ['Storage_1', 'Lviv'],
                                     ['Storage_2', 'Odessa']]

        unreachable_cities = gas_supply(list_city, list_storage, list_active_gas_pipelines)

        self.assertEqual(unreachable_cities, {'Kharkiv'})

        list_city2 = ['Lviv', 'Kyiv', 'Odessa', 'Kharkiv']
        list_storage2 = ['Storage_1', 'Storage_2', 'Storage_3']
        list_active_gas_pipelines2 = []

        unreachable_cities2 = gas_supply(list_city2, list_storage2, list_active_gas_pipelines2)

        self.assertEqual(unreachable_cities2, {'Lviv', 'Kyiv', 'Odessa', 'Kharkiv'})

        list_city3 = ['Lviv', 'Kyiv', 'Odessa', 'Kharkiv']
        list_storage3 = ['Storage_1', 'Storage_2']
        list_active_gas_pipelines3 = [['Lviv', 'Kyiv'], ['Storage_1', 'Lviv']]

        unreachable_cities3 = gas_supply(list_city3, list_storage3, list_active_gas_pipelines3)

        self.assertEqual(unreachable_cities3, {'Odessa', 'Kharkiv'})


if __name__ == '__main__':
    main()
