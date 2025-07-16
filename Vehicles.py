class Car:
    def __init__(self):
        self.name = "Car"
        self.mpg = 30  # miles per gallon

    def fuel_needed(self, distance):
        return distance / self.mpg

    def description(self):
        return f"{self.name} gets {self.mpg} miles per gallon."


class Truck:
    def __init__(self):
        self.name = "Truck"
        self.mpg = 15  # miles per gallon

    def fuel_needed(self, distance):
        return distance / self.mpg

    def description(self):
        return f"{self.name} gets {self.mpg} miles per gallon."


class Motorcycle:
    def __init__(self):
        self.name = "Motorcycle"
        self.mpg = 50  # miles per gallon

    def fuel_needed(self, distance):
        return distance / self.mpg

    def description(self):
        return f"{self.name} gets {self.mpg} miles per gallon."


class Bus:
    def __init__(self):
        self.name = "Bus"
        self.mpg = 8  # miles per gallon

    def fuel_needed(self, distance):
        return distance / self.mpg

    def description(self):
        return f"{self.name} gets {self.mpg} miles per gallon."
