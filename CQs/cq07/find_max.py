"""CQ07: Finding the largest value in a list."""


__author__ = "730574218"


def find_and_remove_max(input: list[int]) -> int:
    """Finds, returns and deletes the largest value in a list."""
    # return -1 if an empty list is provided
    if len(input) == 0: # has to be above anything else, especially max_num definition, because it will try to run it until it reaches the return statement.
        return -1
    max_num: int = input[0] # results in an IndexError if above the length check. 
    # find max_num
    for idx in range(0,len(input)):
        if input[idx] > max_num: # idx in a for range loop is the index of that point in the list, unlike elem in a for loop, which holds the value. Therefore, we need input[idx] here.
            max_num = input[idx]
    # remove max_num
    idx: int = 0
    while idx < len(input): # for loop or for range loop don't work here; instead, we need a while loop. 
        if input[idx] == max_num: # increasing the index in the if block would result in skipping an index since all of the values are shifted over one when an item in a list is removed.
            input.pop(idx)
        else: # need to have the increase of idx in an else block, so that it does not increase if an item is removed.
            idx += 1    
    return max_num
