"""CQ07: max test"""


__author__ = "730574218"


from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_return() -> None:
    a: list[int] = [1,2,3,3,2]
    assert find_and_remove_max(a) == 3

def test_find_and_remove_max_mutate() -> None:
    a: list[int] = [1,2,3,3,2]
    find_and_remove_max(a)
    assert a == [1,2,2]

def test_find_and_remove_max_edge_case() -> None:
    b: list[int] = []
    assert find_and_remove_max(b) == -1