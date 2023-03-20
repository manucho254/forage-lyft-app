from tires.abstract_tire import Tire


class CarriganTire(Tire):
    def __init__(self, four_tires_condition: list):
        """
        - The condition of a single tire can be any number between 0 and 1
        - All the numbers will be stored in the four_tires_condition array
        """
        self.four_tires_condition = four_tires_condition

    def needs_service(self) -> bool:
        return any({x for x in self.four_tires_condition if x > 0.9})
