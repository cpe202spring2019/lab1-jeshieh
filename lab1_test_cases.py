import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        #Tests if value is none
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

        #Test if list is empty
        self.assertEqual(max_list_iter([]), None)

        #Tests if list can spit out right value
        int_list = [1,2,3,5,7,3,44,5,8,90,4,33,4]
        self.assertEqual(max_list_iter(int_list), 90)

        # Tests if list has repeat values
        int_list = [1, 2, 3, 90, 7, 3, 44, 90, 8, 90, 4, 33, ]
        self.assertEqual(max_list_iter(int_list), 90)

        #Tests if max value is at beginning of list
        # Tests if list can spit out right value
        int_list = [429, 2, 3, 5, 7, 3, 44, 5, 8, 90, 4, 33, 3]
        self.assertEqual(max_list_iter(int_list), 429)

        # Tests if max values is at end of list
        int_list = [1, 2, 3, 5, 7, 3, 44, 5, 8, 90, 4, 33, 7393]
        self.assertEqual(max_list_iter(int_list), 90)



    def test_reverse_rec(self):
        #Tests if list it non what does it do
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

        #Tests if it reverses a list of all positives
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

        #Tests if it reverses a list of all negatives
        self.assertEqual(reverse_rec([-5,-1,-4,-5]), [-5,-4,-1,-5])

        #Tests if it reverses a list of repeated numbers
        self.assertEqual(reverse_rec([0, 0, 0]), [0, 0, 0])


    def test_bin_search(self):

        #Tests if binary search can find a target
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

        #Tests if binary search can raise a value error
        with self.assertRaises(ValueError):
            bin_search(4, 0, len(list_val)-1, None)

        # Tests if target is not in list but whole list is searched
        self.assertEqual(bin_search(-8, 0, len(list_val) - 1, list_val), None)

        #Tests if target is not in list but only part of list is searched
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 3
        high = len(list_val) - 1
        self.assertEqual(bin_search(1, low, high, list_val), None)

        #Tests of target is in the middle of the list
        list_val = [1, 2, 3, 4, 5, 6, 7]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, low, high, list_val), 3)

        #Tests if target is at beginning
        list_val = [1, 3, 5, 11, 16, 18, 31, 60]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), 0)

        #Tests if target is at end
        list_val = [1, 3, 5, 11, 16, 18, 31, 60]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(60, low, high, list_val), 7)



if __name__ == "__main__":
        unittest.main()

