import unittest
from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        answer = [1, 2, 3]
        self.assertEqual(selection_sort([3, 2, 1]), answer)

    def test_selection_sort_signed_int(self):
        answer = [-100, 50, 70, 100]
        self.assertEqual(selection_sort([50, 70, -100, 100]), answer)


if __name__ == '__main__':
    unittest.main()
