"""Some happy, little trees!"""

from .turtle import Turtle
from math import pi

__template__ = "https://24ss2.comp110.com/static/turtle/"

DEGREE: float = -pi / 180.0


def main() -> None: ...


def click(x: float, y: float) -> Turtle:
    """Moves turtle to wherever we click on the canvas!"""
    t: Turtle = Turtle()
    t.setSpeed(1000.0)
    t.moveTo(x, y)
    t.turnTo(90 * DEGREE)

    # length: float = 150.0
    # while length > 0.0:
    #    t.forward(length)
    #    t.left(pi / 2.0 - pi / 8.0)
    #    length -= 2.0

    # t.forward(150.0)
    # t.left(pi / 2.0)
    # t.forward(148.0)
    # t.left(pi / 2.0)
    branch(t, y * 0.15, 90 * DEGREE)

    return t


def branch(t: Turtle, length: float, angle: float) -> None:
    t.turnTo(angle)
    t.forward(length)
    # Magic Art Happens Here
    if length > 3.0:
        branch(t, length * 0.75, angle + 35.0 * DEGREE)
        branch(t, length * 0.75, angle - 35.0 * DEGREE)
    t.turnTo(angle + pi)
    t.forward(length)
