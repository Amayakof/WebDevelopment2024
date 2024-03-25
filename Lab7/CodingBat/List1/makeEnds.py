import random
# Given an array of ints,
# return a new array length 2
# containing the first and last elements from the original array.
# The original array will be length 1 or more.

# make_ends([1, 2, 3]) → [1, 3]
# make_ends([1, 2, 3, 4]) → [1, 4]
# make_ends([7, 4, 6, 2]) → [7, 2]

def make_ends(nums):
    return [nums[0], nums[-1]]


if __name__ == '__main__':
    sample_arr = [1, 2, 3, 4, 5, 6]
    nums = random.sample(sample_arr, random.randint(1, 4))
    print(nums)
    print(make_ends(nums))