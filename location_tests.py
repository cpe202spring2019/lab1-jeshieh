import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_eq(self):
        #Tests if eq works
        loc1 = Location('Oakland', -23.2, 2342.3)
        loc2 = Location('Oakland', -23.2, 2342.3)
        self.assertEqual(loc1 == loc2, True)

        #Tests if other object is not of Location type
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = 'SLO, 35.3, -120.7'
        self.assertEqual(loc1 == loc2, False)

        loc1 = Location('Oaland', -23.2, 2342.3)
        loc2 = Location('Oakland', -23.2, 2342.3)
        self.assertEqual(loc1 == loc2, False)

        #Tests if city is different
        loc1 = Location('Oakland', 23.2, 2342.3)
        loc2 = Location('Oakland', -23.2, 2342.3)
        self.assertEqual(loc1 == loc2, False)

        #Tests if latitude is different
        loc1 = Location('Oakland', 23.2, 2342.3)
        loc2 = Location('Oakland', -23.2, 2342.3)
        self.assertEqual(loc1 == loc2, False)

        #Tests if longitude is different
        loc1 = Location('Oakland', -23.2, -2342.3)
        loc2 = Location('Oakland', -23.2, 2342.3)
        self.assertEqual(loc1 == loc2, False)
if __name__ == "__main__":
        unittest.main()
