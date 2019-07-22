import random
import time
import unittest
from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        t = time.time() - self.start_time
        print('{:.3f}'.format(t))

    def test_insertion_sort(self):
        answer = [1, 2, 3]
        self.assertEqual(insertion_sort([3, 2, 1]), answer)

    def test_insertion_sort_signed_int(self):
        answer = [-100, 50, 70, 100]
        self.assertEqual(insertion_sort([50, 70, -100, 100]), answer)

    def test_insertion_sort_random_1000(self):
        data = [random.randint(-100, 100) for _ in range(1000)]
        self.assertEqual(insertion_sort(data), sorted(data))


if __name__ == '__main__':
    unittest.main()
