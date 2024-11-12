"""Summing the elements of a list using different loops."""


__author__ = "730574218"


def w_sum(vals: list[float]) -> float:
    """Sums floats in a list using a while loop."""
    idx: int = 0
    final_value: float = 0.0 # need to have a variable that the value at each index is added to.
    while idx < len(vals):
        final_value += vals[idx]
        idx +=1
    return final_value


def f_sum(vals: list[float]) -> float:
    """Sums floats in a list using a for...in... loop."""
    final_value: float = 0.0
    for elem in vals: 
        final_value += elem # can be += to elem because the value at the specific index becomes the variable elem during that loop.
    return final_value


def f_range_sum(vals: list[float]) -> float:
    """Sums floats in a list using a for...in range loop."""
    final_value: float = 0.0
    for idx in range(0,len(vals)):
        final_value += vals[idx] # cannot be += to idx because a range can skip indices. Instead need to do like the while loop where it's += vals[idx].
    return final_value
