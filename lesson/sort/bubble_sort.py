def bubble_sort(numbers:list):
    for j in range(len(numbers)):
        for i in range(len(numbers)-1-j):
            if numbers[i]>numbers[i+1]:
                numbers[i],numbers[i+1]=numbers[i+1], numbers[i]
    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for i in range(10)]
    print(bubble_sort(nums))


            