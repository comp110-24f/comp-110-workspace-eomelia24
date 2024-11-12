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
        # set-up new list, which self.fish will be set equal to
        copy_fish: list[Fish] = []
        # fish is the element that will be looped over
        # use self.fish to refer to the instance of the object (not attribute)
        for fish in self.fish:
            # fish is elem, . connects fish to age variable of that instance of Fish
            # don't need self
            if fish.age < 4:
                # if fish age is < 4, it is still alive, so it is added to the new list
                copy_fish.append(fish)
        self.fish = copy_fish
        copy_bears: list[Bear] = []
        for bear in self.bears:
            # if bear age is < 6, it is still alive and is added to the new list
            if bear.age < 6:
                copy_bears.append(bear)
        self.bears = copy_bears
        return None

    def bears_eating(self):
        """Number of fish eaten by bears."""
        # while there are >= 5 fish (len of self.fish), the bears will eat
        while len(self.fish) >= 5:
            # within this class, we will use the method remove_fish with argument 3 fish
            self.remove_fish(3)
            # we will loop over each element in self.bears (i.e. each instance of bear)
            for bear in self.bears:
                # call method eat with argument 3 for 3 fish
                bear.eat(3)
        return None

    def check_hunger(self):
        """Checking if a bear dies from starvation."""
        copy_bears: list[Bear] = []
        for bear in self.bears:
            # bears will remain in the ecosystem if their hunger score is not negative
            if bear.hunger_score >= 0:
                # append to the new list if bear has not starved
                copy_bears.append(bear)
        self.bears = copy_bears
        return None

    def repopulate_fish(self):
        """Addition of fish to population through reproduction."""
        # population size is equal to len(self.fish)
        n: int = len(self.fish)
        # number of fish that have been added already
        new_fish: int = 0
        # if number of fish already added is less than n // 2 * 4, while loop will run
        while new_fish < n // 2 * 4:
            # add new fish to self.fish by appending an instantiation of class Fish
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
        print(f"~~~ Day {self.day}: ~~~")
        # len(self.fish) provides the number of fish
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
        # variable for number of loops already completed
        num_loop: int = 0
        # loop 7 times
        while num_loop < 7:
            # method call for one_river_day()
            self.one_river_day()
            num_loop += 1
        return None

    def remove_fish(self, amount: int):
        """Removes a specified amount of fish."""
        # tracks number of loops completed
        loop: int = 0
        # loop until reach the amount of fish specified for removal
        while loop < amount:
            # removes fish at idx 0; works b/c idx assignments shift after one removed
            self.fish.pop(0)
            loop += 1
        return None
