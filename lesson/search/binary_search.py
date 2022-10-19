from typing import List , NewType
IndexNum = NewType('IndexNum', int)

def binary_search(numbers:List[int], value:int)->IndexNum: #use while
    left = 0
    right = len(numbers)-1 #lenは1から　indexは0から
    while left <= right:
        mid = (left + right)//2
        if numbers[mid] == value:
            return mid
        elif numbers[mid]<value:
            left = mid +1
        else:
            right = mid-1
    
    return -1 #if don't find it


def binary_search(numbers:List[int], value:int)->IndexNum: #use Recursion
    def _binary_search(numbers:List[int], value:int, left:IndexNum, right:IndexNum)->IndexNum:
        if left> right:
            return -1
        mid = (left + right)//2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(numbers, value, mid+1, right)
        else :
            return _binary_search(numbers,value, left, mid-1)
    
    return _binary_search(numbers,value, 0,len(numbers)-1)

if __name__ =="__main__":
    




    
