import random
# Given 2 ints, a and b, return their sum.
# However, sums in the range 10..19 inclusive, are forbidden, 
# so in that case just return 20.

# sorta_sum(3, 4) → 7
# sorta_sum(9, 4) → 20
# sorta_sum(10, 11) → 21

def sorta_sum(a, b):
    sum = a + b
    if 10 <= sum <= 19:
        return 20
    
    return sum


if __name__ == '__main__':
    # a = random.randint(1, 100)
    # b = random.randint(1, 100)
    a = 10
    b = 7
    print(a, b)
    print(sorta_sum(a, b))