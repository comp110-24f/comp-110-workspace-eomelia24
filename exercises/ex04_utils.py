"""EX04: Practice with computational thinking."""


__author__: str = "730574218"


def all(list_1: list[int], int_1: int) -> bool:
    match: bool = False
    for elem in list_1:
        if int_1 == elem:
            match = True
        else:
            match = False
    return match

