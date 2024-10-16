"""CQ07: Testing find_max"""


__author__ = "730574218"


from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_return() -> None:
    """Checks if the return value of find_and_remove_max is correct."""
    a: list[int] = [1,2,3,3,2]
    assert find_and_remove_max(a) == 3 # have to put as find_and_remove_max(a) == 3 instead of find_and_remove_max == 3 without an argument. 

def test_find_and_remove_max_mutate() -> None:
    """Checks if find_and_remove_max mutates a list correctly."""
    a: list[int] = [1,2,3,3,2]
    find_and_remove_max(a)
    assert a == [1,2,2]

def test_find_and_remove_max_edge_case() -> None:
    """Checks if find_and_remove_max produces the correct output with an edge case."""
    b: list[int] = []
    assert find_and_remove_max(b) == -1 # same as above; we need to have an argument to have a return value be given, which we can assert should be equal -1 in this case.
    