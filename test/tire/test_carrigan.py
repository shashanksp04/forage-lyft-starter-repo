import unittest
from tire.carrigan import Carrigan

class CarriganTest(unittest):

    # checking for the Carrigan tires when one value is greater than or equal to 0.9
    def test_engine_should_be_serviced(self):
        tire_wear = [0.5,0.6,0.9,0.4]
        car = Carrigan(tire_wear)
        self.assertTrue(car.needs_service())

    # checking for the Carrigan tires when no value is greater than or equal to 0.9
    def test_engine_should_not_be_serviced(self):
        tire_wear = [0.5,0.6,0.7,0.4]
        car = Carrigan(tire_wear)
        self.assertTrue(car.needs_service())