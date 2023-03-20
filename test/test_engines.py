import unittest

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine


class TestCapulet(unittest.TestCase):
    def setUp(self):
        self.current_mileage: int = 0
        self.last_service_mileage: int = 0
        self.capulet: CapuletEngine = None

    def create_capulet(self):
        self.capulet = CapuletEngine(self.current_mileage, self.last_service_mileage)

    def test_engine_should_be_serviced(self):
        self.current_mileage = 40000
        
        self.create_capulet()
        self.assertTrue(self.capulet.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.current_mileage = 20000
        
        self.create_capulet()
        self.assertFalse(self.capulet.needs_service())


class TestSternman(unittest.TestCase):
    def setUp(self):
        self.warning_light_on: bool = False
        self.sternman: SternmanEngine = None

    def create_sternman(self):
        self.sternman = SternmanEngine(self.warning_light_on)

    def test_engine_should_be_serviced(self):
        self.warning_light_on = True

        self.create_sternman()
        self.assertTrue(self.sternman.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.warning_light_on = False

        self.create_sternman()
        self.assertFalse(self.sternman.needs_service())


class TestWilloughby(unittest.TestCase):
    def setUp(self):
        self.current_mileage: int = 0
        self.last_service_mileage: int = 0
        self.sternman: WilloughbyEngine = None

    def create_willoughby(self):
        self.willoughby = WilloughbyEngine(
            self.current_mileage, self.last_service_mileage
        )

    def test_engine_should_be_serviced(self):
        self.current_mileage = 70000

        self.create_willoughby()
        self.assertTrue(self.willoughby.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.current_mileage = 40000

        self.create_willoughby()
        self.assertFalse(self.willoughby.needs_service())


if __name__ == "__main__":
    unittest.main()
