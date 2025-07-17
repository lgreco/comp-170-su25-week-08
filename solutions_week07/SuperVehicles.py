class SuperVehicles:
    def __init__(self, name, mpg):
        """A vehicle is defined by a name that describes its style and its mileage."""
        self.name = name
        self.mpg = mpg  # miles per gallon

    def fuel_needed(self, distance):
        """Computes the amount of fuel needed for a given distance based on the 
        vehicle's fuel consumption."""
        return distance / self.mpg

    def description(self):
        """The Vehicle object can describe itself using the following string. 
        This can also be used as the basis for the __str__ method of the 
        class if we need one so that we can print its objets."""
        return f"{self.name} gets {self.mpg} miles per gallon."


#------------------------------------------------------------------------------#
# Based on the super class Vehicles above, the various specific ale classses in 
# this example can be rewritten as follows. Each class delegates in instantiation 
# method __init__ to the superclass's __init__, providing it with the specific
# vehicle's name and mpg.

class Car(SuperVehicles):
    def __init__(self):
        super().__init__("Car", 30)


class Truck(SuperVehicles):
    def __init__(self):
        super().__init__("Truck", 15)


class Motorcycle(SuperVehicles):
    def __init__(self):
        super().__init__("Motorcycle", 50)


class Bus(SuperVehicles):
    def __init__(self):
        super().__init__("Bus", 8)
