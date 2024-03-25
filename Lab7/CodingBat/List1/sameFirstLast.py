import random
# Given an array of ints,
# return True if the array is length 1 or more, 
# and the first element and the last element are equal.

# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True
 
def same_first_last(nums):
    return (len(nums) >= 1
            and nums[0] == nums[-1])


if __name__ == '__main__':
    sample_arr = [1, 2, 3, 4, 5, 6]
    # nums = random.sample(sample_arr, random.randint(0, 3))
    # nums = [1, 2, 1]
    # nums = [0]
    nums = [1, 2, 4]
    # print(nums)

    print(same_first_last(nums))