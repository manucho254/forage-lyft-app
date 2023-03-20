from serviceable import Serviceable
from datetime import datetime

from engines.abstract_engine import Engine
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

from batteries.abstract_battery import Battery
from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine: Engine = engine
        self.battery: Battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()


class carFactory:
    def create_calliope(
        self,
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        return Car(capulet_engine, spindler_battery)

    def create_glissade(
        self,
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        return Car(willoughby_engine, spindler_battery)

    def create_palindrome(
        self,
        current_date: datetime,
        last_service_date: datetime,
        warning_light_on: bool,
    ) -> Car:

        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        return Car(sternman_engine, spindler_battery)

    def create_rorschach(
        self,
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        return Car(willoughby_engine, nubbin_battery)

    def create_thovex(
        self,
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        return Car(capulet_engine, nubbin_battery)
