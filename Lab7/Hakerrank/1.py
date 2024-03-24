# String split and join
import sys
from unittest import result

def split_and_join(line):
    words = line.split()
    result = '-'.join(words)
    return result


if __name__ == '__main__':
    line = input()
    # line = 'This is my String'
    result = split_and_join(line)
    print(result)