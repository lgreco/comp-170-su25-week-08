class SuperAle:
    def __init__(self, name, abv):
        """An ale is defined by its name and its alcoholic content expressed 
        as an ABV percenteage (alcohol by volume)."""
        self.name = name
        self.abv = abv  # Alcohol by volume

    def alcohol_content(self, volume_in_oz):
        """Returns the alcohol content of a given quantity of ale."""
        return self.abv * volume_in_oz

    def description(self):
        """The Ale object can describe itself using the following string. 
        This can also be used as the basis for the __str__ method of the 
        class if we need one so that we can print its objets."""
        return f"{self.name}: {self.abv * 100:.1f}% ABV"

#------------------------------------------------------------------------------#
# Based on the super class Ale above, the various specific ale classses in this
# example can be rewritten as follows. Each class delegates in instantiation 
# method __init__ to the superclass's __init__, providing it with the specific
# ale's name and ABV.


class PaleAle(SuperAle):
    def __init__(self):
        super().__init__("Pale Ale", 0.055)

class IPA(SuperAle):
    def __init__(self):
        super().__init__("IPA", 0.065)

class Stout(SuperAle):
    def __init__(self):
        super().__init__("Stout", 0.07)

class Porter(SuperAle):
    def __init__(self):
        super().__init__("Porter", 0.06)