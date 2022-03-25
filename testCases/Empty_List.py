import unittest
from updatedsort import bubble_sort_v1

class TestBubbleSortAlgorithm(unittest.TestCase):

    def _test_sort(self, sorting_func, input_list):
        expected_list = sorted(input_list)
        assert sorting_func(input_list) == expected_list
    
    def test_bubble_sort_empty_list(self):
        input_list = []
        self._test_sort(bubble_sort_v1, input_list)