"""Planning a tea party."""


__author__: str = "730574218"


def main_planner(guests: int) -> None:
    """Combine tea party planning functions."""
    print("A Cozy Tea Party for " + str(guests) + " People!") # guests has to be converted to type str.
    print("Tea Bags: " + str(tea_bags(people=guests))) # people parameter from function tea_bags takes guests as the argument.
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)))) # Functions tea_bags and treats require arguments for their parameters.


def tea_bags(people: int) -> int:
    """Determine number of tea bags from number of people."""
    return people * 2


def treats(people: int) -> int:
    """Determine number of treats from number of people."""
    return int(tea_bags(people=people) * 1.5) # int() or round() is required because return type is int while 1.5 is a float.


def cost(tea_count: int, treat_count: int) -> float:
    """Determine cost of buying tea bags and treats."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
    