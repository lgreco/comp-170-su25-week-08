class PaleAle:
    def __init__(self):
        self.name = "Pale Ale"
        self.abv = 0.055 # Alcohol by volume

    def alcohol_content(self, volume_in_oz):
        return self.abv * volume_in_oz

    def description(self):
        return f"{self.name}: {self.abv*100:.1f}% ABV"


class IPA:
    def __init__(self):
        self.name = "IPA"
        self.abv = 0.065 # Alcohol by volume

    def alcohol_content(self, volume_in_oz):
        return self.abv * volume_in_oz

    def description(self):
        return f"{self.name}: {self.abv*100:.1f}% ABV"


class Stout:
    def __init__(self):
        self.name = "Stout"
        self.abv = 0.07 # Alcohol by volume

    def alcohol_content(self, volume_in_oz):
        return self.abv * volume_in_oz

    def description(self):
        return f"{self.name}: {self.abv*100:.1f}% ABV"


class Porter:
    def __init__(self):
        self.name = "Porter"
        self.abv = 0.06 # Alcohol by volume

    def alcohol_content(self, volume_in_oz):
        return self.abv * volume_in_oz

    def description(self):
        return f"{self.name}: {self.abv*100:.1f}% ABV"
