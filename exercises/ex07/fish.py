"""File to define Fish class."""

__author__: str = "730574218"


class Fish:
    """New object called Fish."""

    age: int

    def __init__(self):
        """Initialization of a new fish to the river."""
        # initializes age attribute to value of 0
        self.age = 0
        return None

    def one_day(self):
        """Increasing age for one day in the river."""
        self.age += 1
        return None
