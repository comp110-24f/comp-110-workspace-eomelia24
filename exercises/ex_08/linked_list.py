from __future__ import annotations


"""Lesson on Linked Lists."""

__author__: str = "730574218"


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
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
        return rest


# Still working on it!
def max(head: Node | None) -> int:
    if head is None:
        raise ValueError("Cannot call max with None.")
    if head.next is None:
        raise ValueError("Cannot call max with None.")
    else:
        max_val: int
        if head.next.value > head.value:
            max_val = max(head.next)
            return max_val

    # else:
    # max_val: int = head.value
    # if max_val < max(head.next):
    #     max_val = head.value
    # return max_val
