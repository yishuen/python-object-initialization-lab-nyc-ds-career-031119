import pytest
from ipynb.fs.full.index import *

def test_driver_initialization():
    new_driver = Driver("Dale", "Earnhardt")
    other_driver = Driver("Lady", "Gaga", "Poker")
    assert new_driver.first == "Dale"
    assert new_driver.last == "Earnhardt"
    assert new_driver.favorite_hobby == "driving"
    assert other_driver.favorite_hobby == "Poker"

def test_passenger_initialization():
    new_passenger = Passenger("Rebecca", "Black", "rebecca.black@gmail.com")
    other_passenger = Passenger("Lady", "Gaga", "lady.gaga@littlemonsters.net", 10)
    assert new_passenger.first == "Rebecca"
    assert new_passenger.last == "Black"
    assert new_passenger.rides_taken == 0
    assert other_passenger.email == "lady.gaga@littlemonsters.net"
    assert other_passenger.rides_taken == 10
