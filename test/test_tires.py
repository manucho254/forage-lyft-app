import unittest

from tires.carrigan import CarriganTire
from tires.octoprime import OctoprimeTire


class TestCarrigan(unittest.TestCase):
    def setUp(self):
        self.four_tires_condition: list = []
        self.carrigan: CarriganTire = None

    def create_carrigan(self):
        self.carrigan = CarriganTire(self.four_tires_condition)

    def test_tire_should_be_service(self):
        self.four_tires_condition = [0.1, 0.2, 0.3, 1]

        self.create_carrigan()

        self.assertTrue(self.carrigan.needs_service())

    def test_tire_should_not_be_service(self):
        self.four_tires_condition = [0.4, 0.5, 0.7, 0.8]

        self.create_carrigan()

        self.assertFalse(self.carrigan.needs_service())


class TestOctoprime(unittest.TestCase):
    def setUp(self):
        self.four_tires_condition: list = []
        self.octoprime: OctoprimeTire = None

    def create_octoprime(self):
        self.octoprime = OctoprimeTire(self.four_tires_condition)

    def test_tire_should_be_service(self):
        self.four_tires_condition = [1, 0.8, 0.9, 1]

        self.create_octoprime()

        self.assertTrue(self.octoprime.needs_service())

    def test_tire_should_not_be_service(self):
        self.four_tires_condition = [0, 0.5, 0.5, 0.8]

        self.create_octoprime()

        self.assertFalse(self.octoprime.needs_service())


if __name__ == "__main__":
    unittest.main()
