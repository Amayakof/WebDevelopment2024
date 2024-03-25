import random
# Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 7 
# (every 6 will be followed by at least one 7). Return 0 for no numbers.

# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
    summ = 0
    skip = False
  
    for i in range(len(nums)):
        if nums[i] == 6:
            skip = True
        if not skip:
            summ += nums[i]
        if nums[i] == 7 and skip:
            skip = False
    return summ


if __name__ == '__main__':
    sample_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # nums = random.sample(sample_arr, 6)
    nums = [1, 2, 2, 6, 99, 99, 7] #ans -> 5
    print(nums)
    print(sum67(nums))
