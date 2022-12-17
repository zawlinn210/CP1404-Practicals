"""
Programming Language Class
Estimate: 15 minutes
Actual:   19 minutes
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""
    def __init__(self, field="", typing="", reflection="", year=0):
        """Initialise a Programming Language instance."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check Programming Language is dynamic or not."""
        if self.typing == "Dynamic" or self.typing == "dynamic":
            print(self.field)
            return True
        else:
            return False

    def __str__(self):
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
