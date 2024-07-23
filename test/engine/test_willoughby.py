import unittest
from engine.willoughby_engine import WilloughbyEngine

class CapuletTest(unittest):

    # Checking for the CapuletEngine when current mileage - last_serviced > 60000
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    # Checking for the CapuletEngine when current mileage - last_serviced < 600000
    def test_engine_should_not_be_serviced(self):
        current_mileage = 5999
        last_service_mileage = 0
        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())