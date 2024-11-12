"""Creating a new river."""

__author__: str = "730574218"

from exercises.ex07.river import River

# Instantiates a new object of type River
my_river: River = River(10, 2)

# method call for view_river, taking no arguments
my_river.view_river()

# method call for one_river_week, taking no arguments
my_river.one_river_week()
