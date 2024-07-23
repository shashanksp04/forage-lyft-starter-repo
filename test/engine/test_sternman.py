import unittest
from engine.sternman_engine import SternmanEngine

class CapuletTest(unittest):

   # Checking for the SternmanEngine when warning light is on
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        car = SternmanEngine(warning_light_is_on)
        self.assertTrue(car.needs_service())

    # Checking for the SternmanEngine when warning light is off
    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        car = SternmanEngine(warning_light_is_on)
        self.assertFalse(car.needs_service())