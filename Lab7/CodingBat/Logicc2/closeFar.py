import random
# Given three ints, a b c,
# return True if one of b or c is "close" (differing from a by at most 1),
# while the other is "far", 
# differing from both other values by 2 or more. 
# Note: abs(num) computes the absolute value of a number.

# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True

def close_far(a, b, c):
    if abs(a - b) <= 1:
        if abs(a - c) >= 2 and abs(b - c) >= 2:
            return True
  
    if abs(a - b) <= 1:
        if abs(a - b) >= 2 and abs(b - c) >= 2:
            return True

    return False


if __name__ == '__main__':
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    c = random.randint(-100, 100)
    print(a, b, c)
    print(close_far(a, b, c))