CURRENT_YEAR = 2022
VINTAGE_YEAR = 50


class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __rep__(self):
        return f"{self.name} {self.year} {self.cost}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_YEAR

    def __lt__(self, other):
        return self.year < other.year
