# Given a string,
# return a new string where
# the first and last chars have been exchanged.

def front_back(string):
    if len(string) <= 1:
        return string
    mid = string[1:len(string) - 1]
    return string[-1] + mid + string[0]


if __name__ == '__main__':
    string = "Hello"
    print(front_back(string))
