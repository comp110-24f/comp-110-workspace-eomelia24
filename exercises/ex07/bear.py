"""File to define Bear class."""

__author__: str = "730574218"


class Bear:
    """New object called Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing a new bear in the river ecosystem."""
        # initializes age attribute to value of 0
        self.age = 0
        # initializes hunger_score attribute to value of 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Tracking age and hunger score with one day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Hunger score change based on fish eaten."""
        self.hunger_score += num_fish
        return None


print("completed")
