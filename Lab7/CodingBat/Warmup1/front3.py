#Given a string,
# we'll say that the front is
# the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there.
# Return a new string which is 3 copies of the front.

def front3(string):
    str_front = 3
    if len(string) < str_front:
        str_front = len(string)
    front = string[:str_front]
    return front * 3


if __name__ == '__main__':
    string = input()
    print(front3(string))
