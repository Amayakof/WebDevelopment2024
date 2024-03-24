#Given two int values, return their sum.
# Unless the two values are the same,
# then return double their sum.
def sum_double(a, b):
    sum = a + b

    if a == b:
        sum = sum * 2
    return sum


if __name__ == '__main__':
    a = 1
    b = 3
    print(sum_double(a, b))