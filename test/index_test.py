import unittest2 as unittest
from ipynb.fs.full.index import *

class TestObjectInitialization(unittest.TestCase):

    def test_driver_initialization(self):
        new_driver = Driver("Dale", "Earnhardt")
        other_driver = Driver("Lady", "Gaga", "Poker")
        self.assertEqual(new_driver.first, "Dale")
        self.assertEqual(new_driver.last, "Earnhardt")
        self.assertEqual(new_driver.favorite_hobby, "Driving")
        self.assertEqual(other_driver.favorite_hobby, "Poker")

    def test_passenger_initialization(self):
        new_passenger = Passenger("Rebecca", "Black", "rebecca.black@gmail.com")
        other_passenger = Passenger("Lady", "Gaga", "lady.gaga@littlemonsters.net", 10)
        self.assertEqual(new_passenger.first, "Rebecca")
        self.assertEqual(new_passenger.last, "Black")
        self.assertEqual(new_passenger.rides_taken, 0)
        self.assertEqual(other_passenger.email, "lady.gaga@littlemonsters.net")
        self.assertEqual(other_passenger.rides_taken, 10)
