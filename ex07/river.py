"""File to define River class."""

__author__: str = "730574218"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """New object called River, which will include objects Bear and Fish."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check ages of fish and bears; remove from river at certain age."""
        copy_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age < 4:  # or Fish.age?
                copy_fish.append(fish)
        self.fish = copy_fish
        copy_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age < 6:
                copy_bears.append(bear)
        self.bears = copy_bears
        return None

    def bears_eating(self):
        """Number of fish eaten by bears."""
        while len(self.fish) >= 5:
            self.remove_fish(3)
            for bear in self.bears:
                bear.eat(3)
        return None

    def check_hunger(self):
        """Checking if a bear dies from starvation."""
        copy_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score < 0:
                copy_bears.append(bear)
        self.bears = copy_bears
        return None

    def repopulate_fish(self):
        """Addition of fish to population through reproduction."""
        n: int = len(self.fish)
        new_fish: int = 0
        while new_fish < n // 2 * 4:
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Addition of bears to population through reproduction."""
        n: int = len(self.bears)
        new_bears: int = 0
        while new_bears < n // 2:
            self.bears.append(Bear())
        return None

    def view_river(self):
        """View changes in the river ecosystem day-to-day."""
        print(f"~~~ Day {self.day} ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        num_loop: int = 0
        while num_loop < 7:
            self.one_river_day()
            num_loop += 1
        return None

    def remove_fish(self, amount: int):
        """Removes a specified amount of fish."""
        loop: int = 0
        while loop < amount:
            self.fish.pop(0)
            loop += 1
        return None
