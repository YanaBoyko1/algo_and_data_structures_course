from laba1 import find_k_largest, sorted_numbers
from unittest import TestCase, main

class TestSortedNumbers(TestCase):
    def test_sorted_numbers(self):
        num = [15, 7, 22, 9, 36, 2, 42, 18]
        self.assertEqual(sorted_numbers(num), [2, 7, 9, 15, 18, 22, 36, 42])

class TestFindKLargest(TestCase):
    def test_find_k_largest(self):
        num = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        result = find_k_largest(num, k)
        self.assertEqual(result, (22, 2))
        k_largest, position = result
        self.assertEqual(k_largest, 22)
        self.assertEqual(position, 2)

if __name__ == '__main__':
    main()
