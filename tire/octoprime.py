from tire.tire import Tire

class Octoprime(Tire):

    def __init__ (self, tire_array):
        self.tire_array = tire_array

    def needs_service(self) -> bool:
        sum = 0
        for num in self.tire_array:
            sum += num
        return sum >= 3.0