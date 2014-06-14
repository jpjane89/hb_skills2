import unittest

from skills2 import *

class TestDictOperations(unittest.TestCase):

    def setUp(self):
        self.string1 = "I do not like green eggs and and ham."
        self.list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
        self.list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
        self.words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]

    def test_count_unique(self):
        self.assertEqual(count_unique(self.string1), {'I': 1, 'do': 1, 'not': 1, 'like': 1, 'green': 1, 'eggs':1, 'and': 2, 'ham':1 })

    def test_common_items(self):
        self.assertEqual(common_items(self.list1, self.list2), [2, 6, -5, 8])

    def test_common_items2(self):
        self.assertEqual(common_items(self.list1, self.list2), [2, 6, -5, 8])

    def test_sum_zero(self):
        self.assertEqual(sum_zero(self.list1), [(2, -2), (5, -5), (-5, 5), (5, -5), (-2, 2), (2, -2)])

    def test_sum_zero_no_dup(self):
        self.assertEqual(sum_zero_no_dup(self.list1), [(2, -2), (5, -5)])


if __name__ == '__main__':
    unittest.main()