"""CQ07: find max"""


__author__ = "730574218"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    max_num: int = input[0]
    for idx in range(0,len(input)):
        if input[idx] > max_num:
            max_num = input[idx]
    idx: int = 0
    while idx < len(input):
        if input[idx] == max_num:
            input.pop(idx)
        else:
            idx += 1    
    return max_num
