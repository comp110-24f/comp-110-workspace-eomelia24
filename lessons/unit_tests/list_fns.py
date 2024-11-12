"""LS16"""


__author__ = "730574218"


def get_first(input: list[str]) -> str:
    """Returns the first element in a list."""
    if len(input) == 0: # added because we wanted it to return an empty string if it's an empty list
        return ""
    return input[0] 


def remove_first(input: list[str]) -> None:
    """Removes the first element in a list."""
    input.pop(0) # use parentheses and don't need brackets when using pop


def get_and_remove_first(input: list[str]) -> str:
    """Returns the first element in a list and then removes it."""
    first_element: str = input[0]
    input.pop(0)
    return first_element
