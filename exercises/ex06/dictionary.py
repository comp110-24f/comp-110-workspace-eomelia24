"""EX06: Dictionary Utility Functions."""

__author__: str = "730574218"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    output_dict: dict[str, str] = {}
    for key in input_dict: # can use key because it iterates over the keys in a dictionary.
        if input_dict[key] in output_dict: # must use input_dict[key] because asking if the value at key in input_list is already in the output_list
            raise KeyError("Every key must be unique.")
        output_dict[input_dict[key]] = key # using += does not work for dictionaries; instead must use <dict name>[key] = <value> and it is written as such because we're placing the value in the key position and vice versa. 
    return output_dict    


def favorite_color(input_dict: dict[str, str]) -> str:
    color_freq: dict[str, int] = {}
    for key in input_dict:
        if input_dict[key] in color_freq:
            color_freq[input_dict[key]] += 1
        else:
            color_freq[input_dict[key]] = 1
    fav_freq: int = 0
    fav_color: str = ''
    for key in color_freq:
        if color_freq[key] > fav_freq:
            fav_color = key
    return fav_color


def count(input_list: list[str]) -> dict[str, int]:
    output_dict: dict[str, int] = {}
    for elem in input_list:
        if elem in output_dict:
            output_dict[elem] += 1
        else:
            output_dict[elem] = 1
    return output_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    output_dict: dict[str, list[str]] = {}
    for elem in word_list:
        if elem[0].lower() in output_dict:
            output_dict[elem[0].lower()] += [elem]
        else:
            output_dict[elem[0].lower()] = [elem]
    return output_dict
