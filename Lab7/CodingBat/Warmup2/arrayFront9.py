# Given an array of ints,
# return True if one of the first
# 4 elements in the array is a 9.
# The array length may be less than 4.

#array_front9([1, 2, 9, 3, 4]) → True
#array_front9([1, 2, 3, 4, 9]) → False
#array_front9([1, 2, 3, 4, 5]) → False

def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4

    for i in range(end):
        if nums[i] == 9:
            return True
    return False

if __name__ == '__main__':
    # nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    nums = [0, 8, 7, 6, 5, 4, 3, 2, 1]
    print(array_front9(nums))
