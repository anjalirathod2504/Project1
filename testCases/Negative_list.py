import unittest
from updatedsort import bubble_sort_v1

class TestBubbleSortAlgorithm(unittest.TestCase):

    def _test_sort(self, sorting_func, input_list):
        expected_list = sorted(input_list)
        assert sorting_func(input_list) == expected_list
    
    def test_bubble_sort_negative_numbers_only(self):
        input_list = [-1, -3, -5, -7, -9, -5]
        self._test_sort(bubble_sort_v1, input_list)