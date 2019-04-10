import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_eq(self):
        loc1 = Location('Oakland', -23.2, 2342.3)
        loc2 = Location('Oakland', -23.2, 2342.3)
        self.assertEqual(loc1 == loc2, True)

        loc1 = Location('Oaland', -23.2, 2342.3)
        loc2 = Location('Oakland', -23.2, 2342.3)
        self.assertEqual(loc1 == loc2, False)

        loc1 = Location('Oakland', 23.2, 2342.3)
        loc2 = Location('Oakland', -23.2, 2342.3)
        self.assertEqual(loc1 == loc2, False)















    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
