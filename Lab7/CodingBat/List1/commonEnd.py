# Given 2 arrays of ints, a and b, 
# return True if they have the same first element
# or they have the same last element.
# Both arrays will be length 1 or more.

# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True

def common_end(a, b):
    return (len(a) and len(b) >= 1
            and a == b
            or a[0] == b[0]
            or a[-1] == b[-1])


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [1, 1, 0]
    print(common_end(a, b))
