from unittest import TestCase, main
from src.number_of_islands import num_islands


class TestNumIslands(TestCase):
    def test_num_islands(self):
        grid1 = [
            ["1", "0", "1", "0", "0", "0", "1", "1", "1", "1"],
            ["0", "0", "1", "0", "1", "0", "1", "0", "0", "0"],
            ["1", "1", "1", "1", "0", "0", "1", "0", "0", "0"],
            ["1", "0", "0", "1", "0", "1", "0", "0", "0", "0"],
            ["1", "1", "1", "1", "0", "0", "0", "1", "1", "1"],
        ]
        self.assertEqual(num_islands(grid1), 4)

        grid2 = [
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.assertEqual(num_islands(grid2), 0)

        grid3 = [
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
        ]
        self.assertEqual(num_islands(grid3), 1)


if __name__ == "__main__":
    main()
