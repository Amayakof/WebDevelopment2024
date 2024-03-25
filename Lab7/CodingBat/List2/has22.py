import random
# Given an array of ints,
# return True if the array contains a 2 next to a 2 somewhere.

# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False


if __name__ == '__main__':
    sample_arr = [1, 2, 3, 2, 2]
    nums = random.sample(sample_arr, 3)
    print(nums)
    print(has22(nums))
