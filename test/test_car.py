import unittest
from datetime import datetime

from car import carFactory, Car


car_factory = carFactory()
current_day = datetime.today().date()


class TestCalliope(unittest.TestCase):
    def setUp(self):
        self.current_date: datetime = datetime.today().date()
        self.last_service_date: datetime = datetime.today().date()
        self.current_mileage: int = 0
        self.last_service_mileage: int = 0
        self.car: Car = None

    def create_calliope_car(self):
        self.car = car_factory.create_calliope(
            self.current_date,
            self.last_service_date,
            self.current_mileage,
            self.last_service_mileage,
        )

    def test_battery_should_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 3
        )
        self.create_calliope_car()

        self.assertTrue(self.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 1
        )
        self.create_calliope_car()

        self.assertFalse(self.car.needs_service())

    def test_engine_should_be_serviced(self):
        self.last_service_date = self.current_date
        self.current_mileage = 30001
        self.create_calliope_car()

        self.assertTrue(self.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.last_service_date = self.current_date
        self.current_mileage = 30000
        self.create_calliope_car()

        self.assertFalse(self.car.needs_service())


class TestGlissade(unittest.TestCase):
    def setUp(self):
        self.current_date: datetime = datetime.today().date()
        self.last_service_date: datetime = datetime.today().date()
        self.current_mileage: int = 0
        self.last_service_mileage: int = 0
        self.car: Car = None

    def create_glissade_car(self):
        self.car = car_factory.create_glissade(
            self.current_date,
            self.last_service_date,
            self.current_mileage,
            self.last_service_mileage,
        )

    def test_battery_should_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 3
        )

        self.create_glissade_car()
        self.assertTrue(self.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 1
        )

        self.create_glissade_car()
        self.assertFalse(self.car.needs_service())

    def test_engine_should_be_serviced(self):
        self.last_service_date = self.current_date
        self.current_mileage = 60001

        self.create_glissade_car()
        self.assertTrue(self.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.last_service_date = self.current_date
        self.current_mileage = 60000

        self.create_glissade_car()
        self.assertFalse(self.car.needs_service())


class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.current_date: datetime = datetime.today().date()
        self.last_service_date: datetime = datetime.today().date()
        self.warning_light_on: bool = False
        self.current_mileage: int = 0
        self.last_service_mileage: int = 0
        self.car: Car = None

    def create_glissade_car(self):
        self.car = car_factory.create_glissade(
            self.current_date,
            self.last_service_date,
            self.current_mileage,
            self.last_service_mileage,
        )

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = car_factory.create_palindrome(
            current_day, last_service_date, warning_light_is_on
        )
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        warning_light_is_on = False

        car = car_factory.create_palindrome(
            current_day, last_service_date, warning_light_is_on
        )
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = car_factory.create_palindrome(
            current_day, last_service_date, warning_light_is_on
        )
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = car_factory.create_palindrome(
            current_day, last_service_date, warning_light_is_on
        )
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = car_factory.create_rorschach(
            current_day, last_service_date, current_mileage, last_service_mileage
        )
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = car_factory.create_rorschach(
            current_day, last_service_date, current_mileage, last_service_mileage
        )
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = car_factory.create_rorschach(
            current_day, last_service_date, current_mileage, last_service_mileage
        )
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = car_factory.create_rorschach(
            current_day, last_service_date, current_mileage, last_service_mileage
        )
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = car_factory.create_thovex(
            current_day, last_service_date, current_mileage, last_service_mileage
        )
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = car_factory.create_thovex(
            current_day, last_service_date, current_mileage, last_service_mileage
        )
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = car_factory.create_thovex(
            current_day, last_service_date, current_mileage, last_service_mileage
        )
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = car_factory.create_thovex(
            current_day, last_service_date, current_mileage, last_service_mileage
        )
        self.assertFalse(car.needs_service())


if __name__ == "__main__":
    unittest.main()
