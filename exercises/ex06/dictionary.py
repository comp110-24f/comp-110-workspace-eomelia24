"""EX06: Dictionary Utility Functions."""

__author__: str = "730574218"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values in a dictionary."""
    output_dict: dict[str, str] = {}
    for key in input_dict: # can use key because it iterates over the keys in a dictionary.
        if input_dict[key] in output_dict: # must use input_dict[key] because asking if the value at key in input_list is already in the output_list
            raise KeyError("Every key must be unique.")
        output_dict[input_dict[key]] = key # using += does not work for dictionaries; instead must use <dict name>[key] = <value> and it is written as such because we're placing the value in the key position and vice versa. 
    return output_dict    


def favorite_color(input_dict: dict[str, str]) -> str:
    """Finds the most popular color from a list of names and favorite colors."""
    color_freq: dict[str, int] = {} # initiating an empty dict that can be populated with counts of the different colors
    for key in input_dict:
        if input_dict[key] in color_freq: # checks whether the color is already a key in color_freq and then adds 1 to the count if it is
            color_freq[input_dict[key]] += 1
        else:
            color_freq[input_dict[key]] = 1 # the color is not in the dictionary, so it is added as a new key and the count of 1 is assigned to it
    fav_freq: int = 0 # keeps track of what the highest count of a color is as it loops over the keys in color_freq
    fav_color: str = '' # keeps track of the color with the highest count as it loops over the keys in color_freq
    for key in color_freq:
        if color_freq[key] > fav_freq: # checks whether the count at that key is higher than the current highest count
            fav_freq = color_freq[key] # have to reassign fav_freq to the new count to correctly check the boolean 
            fav_color = key
    return fav_color


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list."""
    output_dict: dict[str, int] = {}
    for elem in input_list: # loops over every element in the list
        if elem in output_dict: # checks whether elem is already in output_dict to determine how it is handled
            output_dict[elem] += 1
        else:
            output_dict[elem] = 1
    return output_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Groups words by their starting letter."""
    output_dict: dict[str, list[str]] = {}
    for elem in word_list:
        if elem[0].lower() in output_dict: # .lower corrects for the words sometimes starting with a capital or a lowercase letter, so that all words with the same starting letter are grouped together
            output_dict[elem[0].lower()] += [elem] # must use [] because otherwise it is not seen as the value being added to a list
        else:
            output_dict[elem[0].lower()] = [elem] 
    return output_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the attendance for every day."""
    if day in attendance: # must use if-else because done differently if a key of that day is already in the dictionary or not
        for key in attendance: # loops over every key
            idx: int = 1
            while idx < len(attendance[key]): # loops over every index in the list that is assigned to the key
                if attendance[key][idx] == student: # checks for the student name at every index of the list of that key
                    attendance = attendance # nothing changes if the student name is aready assigned to that day
                else: 
                    attendance[day] += [student] # if the key is already in the dictionary, but the value is not, it has to be assigned += to a new value in order to keep the previous value(s)
    else:
        attendance[day] = [student] # if the key is not in the dictionary, it must be assigned to the value using = because there is no list for the value to be added to
