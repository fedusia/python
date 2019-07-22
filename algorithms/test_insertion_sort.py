import random
import unittest
from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        answer = [1, 2, 3]
        self.assertEqual(insertion_sort([3, 2, 1]), answer)

    def test_insertion_sort_signed_int(self):
        answer = [-100, 50, 70, 100]
        self.assertEqual(insertion_sort([50, 70, -100, 100]), answer)

    def test_insertion_sort_random(self):
        data = [random.randint(-100, 100) for _ in range(100)]
        self.assertEqual(insertion_sort(data), sorted(data))


if __name__ == '__main__':
    unittest.main()
