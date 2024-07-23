import unittest
from datetime import datetime
from battery.splinder import SplinderBattery

class SplinderTest(unittest.TestCase):

     # Checking for the SplinderBattery when current date - last_service_date > 3 years
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        car = SplinderBattery(today,last_service_date)
        self.assertTrue(car.needs_service())

    # Checking for the SplinderBattery when current date - last_service_date < 3 years
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        car = SplinderBattery(today, last_service_date)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()

