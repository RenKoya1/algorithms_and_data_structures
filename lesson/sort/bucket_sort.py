from typing import List
import insertion_sort

def bucket_sort(numbers:List[int])->List[int]:
    len_numbers = len(numbers)
    max_num = max(numbers)
    bucket_size = max_num//len_numbers

    buckets = [[] for _ in range(bucket_size)]
    for num in numbers:
        i = num//bucket_size
        if i !=bucket_size:
            buckets[i].append(num)
        else:
            buckets[bucket_size-1].append(num)

    for i in range(bucket_size):
        insertion_sort.insertion_sort(buckets[i])
    
    result =[]
    for i in range(bucket_size):
        result +=buckets[i]
    
    return result

if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for i in range(10)]
    print(bucket_sort(nums))