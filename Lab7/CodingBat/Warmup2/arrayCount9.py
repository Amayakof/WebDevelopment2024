#Given an array of ints,
# return the number of 9's in the array.

def array_count9(nums):
    counter = 0
    for num in nums:
        if num == 9:
            counter += 1

    return counter

if __name__ == '__main__':
    nums = [9, 8, 9, 6, 5, 4, 9, 2, 1]
    print(array_count9(nums))

