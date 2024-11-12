from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    """get_first should return first element."""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert get_first(dog_breeds) == "husky" # RV should be husky, so assert and use a boolean to check


def test_remove_first_return_value() -> None:
    """remove_first should return None"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert remove_first(dog_breeds) == None # not particularly useful test because we want to know if it's removing the first element, not just that it's returning None.


def test_remove_first_behavior() -> None:
    """Remove_first should remove the first element from the input list."""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    remove_first(dog_breeds)
    assert dog_breeds == ["golden", "poodle", "lab"]

 
def test_get_first_edge_case() -> None:
    """get_first called on an empty list should return "". """
    # could do two lines using inp: list[str] = [] OR do as one like below.
    assert get_first([]) == "" # returns error, index out of range
