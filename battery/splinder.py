from battery import battery


class SplinderBatter(battery):
    
    def __init__(self,last_service_date, current_date):
        super().__init()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return self.current_date - self.last_service_date > 2