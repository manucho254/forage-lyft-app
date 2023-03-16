from batteries.abstract_battery import Battery
from datetime import datetime


class SpindlerBattery(Battery):
    def __init__(self, current_date: datetime, last_service_date: datetime):
        self.current_date: datetime = current_date
        self.last_service_date: datetime = last_service_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 2
        )
        return service_threshold_date < self.current_date
