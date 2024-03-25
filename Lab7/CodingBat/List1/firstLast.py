import random
# Given an array of ints,
# return True if 6 appears
# as either the first or last element in the array.
# The array will be length 1 or more.

# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False

def first_last6(nums):
    return (nums[0] == 6 or nums[-1] == 6)


if __name__ == '__main__':
    sample_arr = [1, 2, 3, 6, 6, 6]
    nums = random.sample(sample_arr, 6)
    print(nums)
    print(first_last6(nums))
