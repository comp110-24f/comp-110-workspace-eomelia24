"""An example of recursive functions."""

__author__ = "730574218"


def factorial(n: int) -> int:
    """Compute the factorial of n."""
    if n == 0 or 1:  # n == 0 returns 1 just because how factorials work
        return 1
    else:
        return n * factorial(n - 1)  # factorial(3) -> 6, factorial(4) -> 24, and so on
