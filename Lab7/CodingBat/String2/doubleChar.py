# Given a string,
# return a string where for every char in the original,
# there are two chars.

# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
    new_str= ""
    for c in str:
        new_str += c*2
    return new_str


if __name__ == '__main__':
    str1 = "Korovka"
    print(double_char(str1))