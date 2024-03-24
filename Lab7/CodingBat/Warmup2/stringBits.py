# Given a string,
# return a new string made of
# every other char starting with the first,
# so "Hello" yields "Hlo".

def string_bits(str):
    new_string = ""
    for i in range(len(str)):
        if i % 2 == 0:
            new_string += str[i]
    return new_string

if __name__ == '__main__':
    str = "abc"
    print(string_bits(str))

