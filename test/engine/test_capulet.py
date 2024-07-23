import unittest
from engine.capulet_engine import CapuletEngine

class CapuletTest(unittest):

    # Checking for the CapuletEngine when current mileage - last_serviced > 30000
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    # Checking for the CapuletEngine when current mileage - last_serviced < 30000
    def test_engine_should_not_be_serviced(self):
        current_mileage = 2999
        last_service_mileage = 0
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())