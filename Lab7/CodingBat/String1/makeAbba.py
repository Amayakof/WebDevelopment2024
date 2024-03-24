# Given two strings, a and b,
# return the result of putting them together
# in the order abba,
# e.g. "Hi" and "Bye" returns "HiByeByeHi".

# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'

def make_abba(a, b):
    return a + b * 2 + a


if __name__ == '__main__':
    a = "io"
    b = "i"
    c = "mio"
    #my Tg ;)
    print(make_abba(a, b) + c)
