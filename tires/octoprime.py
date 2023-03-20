from tires.abstract_tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, four_tires_condition: list):
        """ 
           - The condition of a single tire can be any number between 0 and 1
           - All the numbers will be stored in the four_tires_condition array
        """
        self.four_tires_condition = four_tires_condition

    def needs_service(self) -> bool:
        return sum(self.four_tires_condition) >= 3
