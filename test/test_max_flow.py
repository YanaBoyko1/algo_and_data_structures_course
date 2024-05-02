from unittest import TestCase, main
from max_flow import calculate_max_flow, ford_fulkerson

class TestMaxFlow(TestCase):
    def test_calculate_max_flow(self):
        expected_max_flow = 51
        actual_max_flow = calculate_max_flow('roads.csv')
        self.assertEqual(actual_max_flow, expected_max_flow)

    def test_ford_fulkerson(self):
        graph = {
            'F1': {'X1': 10, 'X2': 25},
            'F2': {'X1': 11, 'X2': 5, 'X3': 7},
            'F3': {'X3': 6},
            'X1': {'S1': 10, 'S2': 8},
            'X2': {'S2': 9, 'S3': 11},
            'X3': {'S3': 7, 'S4': 8, 'S5': 30},
            'S1': {},
            'S2': {},
            'S3': {},
            'S4': {},
            'S5': {}
        }

        max_flow = ford_fulkerson(graph, 'F1', 'S1')
        self.assertEqual(max_flow, 10)

if __name__ == '__main__':
    main()
