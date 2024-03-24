# Given a string,
# return a version without the first and last char,
# so "Hello" yields "ell".
# The string length will be at least 2.

# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'

def without_end(str):
    new_str = str[1: -1]
    if len(new_str) >= 2:
        return new_str


if __name__ == '__main__':
    str = "l'Amoure"
    print(without_end(str))

