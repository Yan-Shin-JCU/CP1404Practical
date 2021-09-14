"""
CP1404/CP5632 Practical
Car class
"""
from prac_08.car import Car


class SilverServiceTaxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Car."""
        self.fanciness = fanciness
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km * fanciness
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(super().__str__(),
                                                                                      self.current_fare_distance ,
                                                                                      SilverServiceTaxi.price_per_km *
                                                                                      self.fanciness,
                                                                                      self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return SilverServiceTaxi.price_per_km * self.current_fare_distance * self.fanciness

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
