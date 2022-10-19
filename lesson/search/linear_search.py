from typing import List , NewType
IndexNum = NewType('IndexNum', int)

def linear_search(numbers:List[int], value: int) ->IndexNum:#　return index
    for i in range(len(numbers)):
        if numbers[i] == value:
            return i
    return -1#if don't find it
