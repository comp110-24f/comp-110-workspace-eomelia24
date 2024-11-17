"""EX08: Using Recursive Calls."""

from __future__ import annotations


__author__: str = "730574218"


class Node:
    """Class object creation of Node."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initiation of class Node."""
        self.value = value
        self.next = next

    def __str__(self) -> str:  # magic method
        """Produce a string representation of a linked list."""
        # use if trying to have output of certain class as a str.
        rest: str = "TODO"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)  # can be this instead: self.next.__str__()
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
# last Node is first one created
print(one)  # output odd without str function: __main__ is module, Node object
# noted at which location - a hexadecimal
print(str(courses))
print(courses)


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base Case: when head is the last node
    #   return its value
    # Recursive Case:
    #   Figure out the last node (recursive call)
    #   in the "rest of the list"
    #   return this value
    print(f"Enter last ({head.value})")  # just to show what's going on
    if head.next is None:  # base case
        print(f"Return base case: {head.value}")  # just to show what's going on
        return head.value
    else:  # recursive case
        rest: int = last(head.next)
        print(f"Return recur: {head.value} -> {rest}")  # just to show what's going on
        return rest


print(last(two))  # expect to print 2; base case
print(last(one))  # expect to print 2; recursive case
print(last(courses))  # expect to print 301; recursive case


def value_at(head: Node | None, index: int) -> int:
    """Finds a Node at index and returns its value."""
    # Edge case:
    #   if the list is empty, raise IndexError
    # Base case:
    #   when reaching specified Node, return its value
    # Recursive case:
    #   find the Node at index and return its value
    if head is None:  # edge case
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:  # base case
        return head.value
    else:  # recursive case
        rest: int = value_at(head.next, index - 1)
        # subtract 1 from index for every loop b/c trying to progress toward base case
        return rest


def max(head: Node | None) -> int:
    """Return the value of the Node with the maximum value in the linked list."""
    # Edge case:
    #   value of head is None
    #   raise a ValueError
    if head is None:
        raise ValueError("Cannot call max with None.")
    # Base case:
    #   if it is the last Node
    #   return its value
    if head.next is None:
        return head.value
    # Recursive case:
    #   set max_val to current Node value
    #   recursively call head.next and compare to max_val
    #   if larger, set max_val equal to it
    #   return max_val
    else:
        max_val: int = head.value
        if max(head.next) > max_val:
            max_val = max(head.next)
        return max_val


def linkify(items: list[int]) -> Node | None:
    """Assign Nodes the values of a list of ints."""
    # Edge case:
    #   an empty input list
    #   return None
    if items == []:
        return None
    # Base case:
    #   when items has a length of 1
    #   create Node with value = items[0] and next = None
    if len(items) == 1:
        return_val = Node(items[0], None)
    # Recursive case:
    #   create Node with value = items[0] and
    #   next = recursive call with slice subscription
    #       slice subscription shortens list every time linkify is called
    else:
        return_val = Node(items[0], linkify(items[1:]))
    # print head using to_str function
    #   print rather than return because return must be Node | None, not str
    # return head, which is Node | None
    print(to_str(return_val))
    return return_val


def scale(head: Node | None, factor: int) -> Node | None:
    """Scale a linked list by a specified factor."""
    # Edge case:
    #   if value of head is None
    #   return None
    if head is None:
        return None
    # Base case:
    #   if last Node in linked list
    #   return Node with value scaled by factor and next = None
    if head.next is None:
        return Node(head.value * factor, None)
    # Recursive case:
    #   recursively call scale for variable rest
    #   print a Node with a scaled value and next = rest
    #       use to_str to convert to a str
    #   return the same Node without being converted to a str
    else:
        rest: Node | None = scale(head.next, factor)
        print(to_str(Node(head.value * factor, rest)))
        return Node(head.value * factor, rest)
