from CQs.cq04.concatenation import concat # function imports should come first, followed by docstring and the author variable.

from CQs.cq04.coordinates import get_coords


"""CQ04 Visualize: Combines concatenation and coordinates."""


__author__ = "730574218"


x: str = "123"
y: str = "abc"


print(concat(x,y))


get_coords(x,y)