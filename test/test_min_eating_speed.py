from src.min_eating_speed import min_eating_speed
from unittest import TestCase, main

class TestMinEatingSpeed(TestCase):
    def test_min_eating_speed(self):
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(min_eating_speed(piles, h), 4)

    def test_min_eating_speed_2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(min_eating_speed(piles, h), 30)

    def test_min_eating_speed_3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(min_eating_speed(piles, h), 23)


if __name__ == '__main__':
    main()
