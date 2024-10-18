"""EX05: Practice with utility functions."""

__author__ = "730574218"


def only_evens(input_list: list[int]) -> list[int]:
    """Returns a list of only even ints without mutating input_list."""
    even_list: list[int] = []
    for elem in input_list:
        if elem % 2 == 0: # if the remainder equals 0, then it is even whereas if it equals 1, it is odd
            even_list.append(elem)
    return even_list # even_list stays an empty list if input_list is an empty list.


def sub(input_list: list[int], idx_start: int, idx_end: int) -> list[int]:
    """Returns a subunit of input_list."""
    output_list: list[int] = []
    if input_list == []:
        return []
    if idx_start < 0: # if a negative value is the argument for idx_start, it will be updated to be equal to 0.
        idx_start = 0
    if idx_end > len(input_list): # should not be elif because it is possible that idx_start and idx_end will both need to be updated to prevent an IndexError.
        idx_end = len(input_list) # if the argument for idx_end is greater than the length of input_list, it will be updated to be equal to the length of input_list.
    current_idx: int = idx_start # we do not necessarily want to start at the beginning of the list, so current_idx should be equal to idx_start.
    while current_idx < idx_end: # because we are not necessarily looping over every index in the list, cannot set current_idx < len(input_list); instead, we need to compare to idx_end.
        output_list.append(input_list[current_idx])
        current_idx += 1
    return output_list


def add_at_index(input_list: list[int], elem: int, idx: int) -> None:
    """Inserts an element into a list at a specific index."""
    if idx < 0 or idx > len(input_list): # can use or operator since both would raise the same IndexError. 
        raise IndexError("Index is out of bounds for the input list")
    input_list.append(0) # need a placeholder value for the added index.
    current_idx: int = len(input_list) - 2 # must be -2 because len(input_list) - 1 would bring us to the last index (the one that was added) and then we need to move one earlier to begin moving the list values to the right.
    while current_idx >= idx: # must be >= because we want to move the element at the target index to the right to clear up space for the new element to be added at that index.
        input_list[current_idx + 1] = input_list[current_idx] # adds the element at current_idx to the next index to the right.
        current_idx -= 1 # moving right to left in order to not lose any of the elements in the list.
    input_list[idx] = elem # once everything is moved, the new element can be added at that spot.
