import random
# Given an int array length 2,
# return True if it contains a 2 or a 3.

# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

def has23(nums):
    return nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3


if __name__ == '__main__':
    sample_arr = [1, 2, 3, 4, 5, 6]
    nums = random.sample(sample_arr, 2)
    print(nums)
    print(has23(nums))
