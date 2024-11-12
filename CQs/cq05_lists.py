"""Mutating functions."""


__author__ = "730574218"


def manual_append(int_list: list[int], list_add: int) -> None:
    """Adds a value to the end of the list."""
    int_list.append(list_add)


def double(int_list: list[int]) -> None:
    """Doubles the values in a list."""
    index: int = 0
    while index < len(int_list):
        int_list[index] *= 2 # need to set it equal to its original value * 2. Won't change if it's just int_list[index] * 2.
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1) # prints [2,4,6], the doubled version, even though list_2 was mutated because they refer to the same list id.
print(list_2)