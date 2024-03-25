import random
# Return the number of even ints in the given array.
# Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    counter = 0
    for i in nums:
        if i % 2 == 0:
            counter += 1
    return counter


if __name__ == '__main__':
    sample_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums = random.sample(sample_arr, 6)
    print(nums)
    print(count_evens(nums))

