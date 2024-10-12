"""EX04: Practice with computational thinking."""


__author__: str = "730574218"


def all(int_list: list[int], num: int) -> bool:
    """Determines whether all values in a list are equal to one int."""
    match: bool = False
    for elem in int_list:
        if num == elem:
            match = True
        else: # need an else block.
            match = False 
            return match # must have a return value here, so that function exits; otherwise, will loop and if the next value is equal to num, it will return True.
    return match


def max(input: list[int]) -> int:
    """Finds the largest value in a list of ints."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List") # takes you out of the function, like a return value does.
    max_num: int = input[0] # may have negative numbers, so cannot start with max_num = 0. 
    for elem in input:
        if max_num < elem: # must use elem instead of input because input is the entire list while elem takes on the value at one location in the list at a time.
            max_num = elem
    return max_num    


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if two lists are the same."""
    equal: bool = False
    idx_1: int = 0
    idx_2: int = 0 # need to have two index variables, one for each list.
    if len(list_1) != len(list_2): # need an if statement so that if the lengths do not equal each other, the function will exit, returning False.
        equal = False
    elif len(list_1) == 0: # need an elif for the case where both lists are empty in order for it to return as True.
        equal = True    
    else: # use an else block because there is only one other option after the if block - that the lengths of the lists are equal and they are not empty, in which case the while loop can be run.
        while idx_1 < len(list_1): # have to use a while loop to compare the values of two lists because the for loop looks at one list.
            equal = (list_1[idx_1] == list_2[idx_2]) # statement comparing the values returns a bool, so equal comes out as either True or False.
            idx_1 += 1
            idx_2 += 1
    return equal 


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Appends one list to the end of another."""
    for elem in list_2: # use for loop because appending list_2 to list_1 leaves the brackets. Appending each elem, however, adds them as individual items into the list.
        list_1.append(elem)
