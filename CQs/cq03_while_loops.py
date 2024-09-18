"""Practice using while loops."""


__author__ = "730574218"


def num_instances(phrase: str, search_char: str) -> None: # returns None because there is no return statement; instead prints Count
    """Count the number of instances of a character in a phrase."""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if search_char == phrase[index]: # need to use == to do the boolean because I'm not assigning a value to search_char
            count = count + 1
        else:
            count = count
        index = index + 1 # in the while block, but outside if and else blocks so that it will increase and not loop infinitely on the first letter   
    print(count)
