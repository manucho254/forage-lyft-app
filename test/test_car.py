import unittest
from datetime import datetime

from car import carFactory, Car


car_factory = carFactory()
current_day = datetime.today().date()


class TestCalliope(unittest.TestCase):
    def setUp(self):
        """initialize the function class with the values below as defaults"""
        self.current_date: datetime = datetime.today().date()
        self.last_service_date: datetime = datetime.today().date()
        self.current_mileage: int = 0
        self.last_service_mileage: int = 0
        self.car: Car = None

    def create_calliope_car(self):
        """function to create a car of type calliope"""
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
        """initialize the function class with the values below as defaults"""
        self.current_date: datetime = datetime.today().date()
        self.last_service_date: datetime = datetime.today().date()
        self.current_mileage: int = 0
        self.last_service_mileage: int = 0
        self.car: Car = None

    def create_glissade_car(self):
        """function to create a car of type glissade"""
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
        """initialize the function class with the values below as defaults"""
        self.current_date: datetime = datetime.today().date()
        self.last_service_date: datetime = datetime.today().date()
        self.warning_light_on: bool = False
        self.car: Car = None

    def create_palindrome_car(self):
        """function to create a car of type palindrome"""
        self.car = car_factory.create_palindrome(
            self.current_date, self.last_service_date, self.warning_light_on
        )

    def test_battery_should_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 5
        )

        self.create_palindrome_car()
        self.assertTrue(self.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 2
        )

        self.create_palindrome_car()
        self.assertFalse(self.car.needs_service())

    def test_engine_should_be_serviced(self):
        self.last_service_date = self.current_date
        self.warning_light_on = True

        self.create_palindrome_car()
        self.assertTrue(self.car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.last_service_date = self.current_date

        self.create_palindrome_car()
        self.assertFalse(self.car.engine.needs_service())


class TestRorschach(unittest.TestCase):
    def setUp(self):
        """initialize the function class with the values below as defaults"""
        self.current_date: datetime = datetime.today().date()
        self.last_service_date: datetime = datetime.today().date()
        self.current_mileage: int = 0
        self.last_service_mileage: int = 0
        self.car: Car = None

    def create_rorschach_car(self):
        """function to create a car of type rorschach"""
        self.car = car_factory.create_rorschach(
            self.current_date,
            self.last_service_date,
            self.current_mileage,
            self.last_service_mileage,
        )

    def test_battery_should_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 5
        )

        self.create_rorschach_car()
        self.assertTrue(self.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 3
        )

        self.create_rorschach_car()
        self.assertFalse(self.car.needs_service())

    def test_engine_should_be_serviced(self):
        self.last_service_date = self.current_date
        self.current_mileage = 60001

        self.create_rorschach_car()
        self.assertTrue(self.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.last_service_date = self.current_date
        self.current_mileage = 60000

        self.create_rorschach_car()
        self.assertFalse(self.car.needs_service())


class TestThovex(unittest.TestCase):
    def setUp(self):
        """initialize the function class with the values below as defaults"""
        self.current_date: datetime = datetime.today().date()
        self.last_service_date: datetime = datetime.today().date()
        self.current_mileage: int = 0
        self.last_service_mileage: int = 0
        self.car: Car = None

    def create_thovex_car(self):
        """function to create a car of type thovex"""
        self.car = car_factory.create_thovex(
            self.current_date,
            self.last_service_date,
            self.current_mileage,
            self.last_service_mileage,
        )

    def test_battery_should_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 5
        )

        self.create_thovex_car()
        self.assertTrue(self.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 3
        )

        self.create_thovex_car()
        self.assertFalse(self.car.needs_service())

    def test_engine_should_be_serviced(self):
        self.last_service_date = self.current_date
        self.current_mileage = 30001

        self.create_thovex_car()
        self.assertTrue(self.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.last_service_date = self.current_date
        self.current_mileage = 30000

        self.create_thovex_car()
        self.assertFalse(self.car.needs_service())


if __name__ == "__main__":
    unittest.main()
