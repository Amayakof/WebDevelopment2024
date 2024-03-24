# Given 2 strings, a and b,
# return the number of the positions
# where they contain the same length 2 substring.
# So "xxcaazz" and "xxbaaz" yields 3,
# since the "xx", "aa", and "az"
# substrings appear in the same place in both strings.

def string_match(a, b):
    shortest = min(len(a), len(b))
    counter = 0
    for i in range(shortest - 1):
        a_substr = a[i:i + 2]
        b_substr = b[i:i + 2]
        if a_substr == b_substr:
            counter = counter + 1
    return counter


if __name__ == '__main__':
    a = 'abcdefg'
    b = 'abjdefp'
    print(string_match(a, b))