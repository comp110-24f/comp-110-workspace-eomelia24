"""EX05: Testing utils."""

__author__ = "730574218"


from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_edge() -> None:
    """Tests that only_evens returns [] when given an empty list."""
    a: list[int] = []
    assert only_evens(a) == []

def test_only_evens_rv() -> None:
    """Tests the return value of only_evens."""
    b: list[int] = [-10, 15, 0, 14]
    assert only_evens(b) == [-10, 0, 14]

def test_only_evens_mutate() -> None:
    """Tests that only_evens does not mutate input_list."""
    b: list[int] = [-10, 15, 0, 14]
    only_evens(b) # need to call the function with argument b as the list to ensure the function does not modify list b.
    assert b == [-10, 15, 0, 14]


def test_sub_edge() -> None:
    """Tests that sub returns [] when given an empty list."""
    a: list[int] = []
    assert sub(a, 0, 8) == [] # need to have the idx_start and idx_end arguments when calling the function, even if return value should be []

def test_sub_rv() -> None:
    """Tests the return value of sub."""
    b: list[int] = [8, 7, 6, 5, 4, 3, 2, 1]
    assert sub(b, -3, 5) == [8, 7, 6, 5, 4]

def test_sub_mutate() -> None:
    """Tests that sub does not mutate input_list."""
    b: list[int] = [8, 7, 6, 5, 4, 3, 2, 1]
    sub(b, -3, 5)
    assert b == [8, 7, 6, 5, 4, 3, 2, 1]


def test_add_at_index_edge() -> None:
    """Tests that add_at_index raises an IndexError when given an invalid index."""
    a: list[int] = []
    with pytest.raises(IndexError): # need to use this special pytest to check for an IndexError.
        add_at_index(a, 15, 2)

def test_add_at_index_rv() -> None:
    """Tests that add_at_index returns None."""
    b: list[int] = [15, 20, 30]
    assert add_at_index(b, 25, 2) == None # this should be checking for a return value of None, rather than checking if the list was mutated.

def test_add_at_index_mutate() -> None:
    """Tests that add_at_index mutates the list correctly."""
    b: list[int] = [15, 20, 30]
    add_at_index(b, 25, 2)
    assert b == [15, 20, 25, 30] # the function also works if adding an elem to the end of the list.
    