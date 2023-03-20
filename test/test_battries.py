import unittest
from datetime import datetime

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery


class TestNubbin(unittest.TestCase):
    def setUp(self) -> None:
        self.current_date: datetime = datetime.today().date()
        self.last_service_date: datetime = datetime.today().date()
        self.nubbin: NubbinBattery = None

    def create_nubbin_battery(self):
        self.nubbin = NubbinBattery(self.current_date, self.last_service_date)

    def test_battery_should_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 5
        )

        self.create_nubbin_battery()
        self.assertTrue(self.nubbin.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 3
        )

        self.create_nubbin_battery()
        self.assertFalse(self.nubbin.needs_service())


class TestSpindler(unittest.TestCase):
    def setUp(self) -> None:
        self.current_date: datetime = datetime.today().date()
        self.last_service_date: datetime = datetime.today().date()
        self.spindler: SpindlerBattery = None

    def create_spindler_battery(self):
        self.spindler = SpindlerBattery(self.current_date, self.last_service_date)

    def test_battery_should_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 4
        )

        self.create_spindler_battery()
        self.assertTrue(self.spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 2
        )

        self.create_spindler_battery()
        self.assertFalse(self.spindler.needs_service())


if __name__ == "__main__":
    unittest.main()
