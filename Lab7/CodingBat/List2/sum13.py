from typing import List
# Return the sum of the numbers in the array,
# returning 0 for an empty array.
# Except the number 13 is very unlucky,
# so it does not count and numbers that come immediately after a 13 also do not count.

# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
    counter = 0
    t = 0
    while t < len(nums):
        if nums[t] == 13:
            t += 1
        else:
            counter += nums[t]
        t += 1
    return counter


# def sum13(nums):
#     total = 0
#     skip = False
#     for num in nums:
#         if skip:
#             skip = False
#             continue
#         if num == 13:
#             skip= True
#             continue
#         total += num
#     return total


if  __name__ == '__main__':
    nums: List[int] = [13, 1, 2, 3]
    print(sum13(nums))
    