# Return the "centered" average of an array of ints, 
# which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array. 
# If there are multiple copies of the smallest value, ignore just one copy, 
# and likewise for the largest value. Use int division to produce the final average. 
# You may assume that the array is length 3 or more.

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
    nums.sort() #[1, 2, 2, 3, 3, 4]
    new_arr = nums[1:-1] #[2, 2, 3, 3, 4]
    print(new_arr)
    return int(sum(new_arr) / len(new_arr))
    # return sum(new_arr)//len(new_arr) #14//5 -> 2


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 2, 3]
    print(centered_average(nums))
