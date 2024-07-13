
from car import Car

from engine import CapuletEngine, SternmanEngine, WilloughbyEngine

from battery import SplinderBattery, NubbinBattery

from datetime import date

class Carfactory():

    def __init__(self):
        pass
    
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(CapuletEngine(current_mileage,last_service_mileage),SplinderBattery(last_service_date,current_date))
    
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(WilloughbyEngine(current_mileage,last_service_mileage),SplinderBattery(last_service_date,current_date))
    
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        return Car(SternmanEngine(warning_light_on),SplinderBattery(last_service_date,current_date))
    
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(WilloughbyEngine(current_mileage,last_service_mileage),NubbinBattery(last_service_date,current_date))

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(CapuletEngine(current_mileage,last_service_mileage),NubbinBattery(last_service_date,current_date))
