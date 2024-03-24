import random
# Given a number n,
# return True if n is in the range 1..10, inclusive. 
# Unless outside_mode is True, in which case return True
# if the number is less or equal to 1, or greater or equal to 10.

def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    return 1 <= n or n >= 10


if __name__ == '__main__':
    n = random.randint(1, 10)
    outside_mode = random.choice([True, False])
    print(n, outside_mode)
    print(in1to10(n, outside_mode))