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
        return head.value
    else:
        max_val: int = head.value
        if max(head.next) > max_val:
            max_val = max(head.next)
        return max_val  # current output is 20

    # else:
    # max_val: int = head.value
    # if max_val < max(head.next):
    #     max_val = head.value
    # return max_val


def linkify(items: list[int]) -> Node | None:
    if items == []:
        return None
    head: Node = Node(items[0], None)
    # if head.next is None:
    #    rest: Node | None = linkify(items[])
    if len(items) == 1:
        head: Node = Node(items[0], None)
    else:
        head: Node = Node(items[0], linkify(items[1:]))
    print(to_str(head))
    return head
    # Go through list and create a Node for each item
    #   Value should be
    # Return Node that is connected to all the others
    # head: Node = Node(items[0], None) # wrong!
    # idx: int = 0
    # head: Node | None = Node(items[idx], Node(idx + 1, None))

    # idx: int = 0
    # if idx == len(items) - 1:
    #    current_val: int = items[idx]
    #    new_node: Node | None = Node(current_val, None)
    #    return new_node
    # if idx < len(items):
    #    current_val: int = items[idx]
    #    items = items[1:]
    #    new_node: Node | None = Node(current_val, linkify(items))
    #    return new_node

    # new_node: Node = Node(items[idx], linkify(items[]))
    # num: int = 0

    # rest: Node | None = linkify(items)
    # if items == []:
    # raise IndexError("List is empty.")
    # else:
    # start: int = 0
    # end: int = len(items) + 1
    # rest: Node | None = linkify(start + 1, end):
    # return linkify([head.value, head.next.value])


def scale(head: Node | None, factor: int) -> Node | None:
    if head is None:
        return None
    if head.next is None:
        return None
    else:
        first: int = head.value * factor
        rest: Node | None = scale(head.next, factor)
        #    head.value = head.value * factor
        #    scaled: Node | None = scale(head.next, factor)
        return Node(first, rest)
