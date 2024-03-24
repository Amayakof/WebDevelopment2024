#Given 2 ints, a and b,
# return True if one of them is 10
# or if their sum is 10.

def makes10(a, b):
  if a == 10 or b == 10 or a+b == 10:
    return True
  else:
    return False


if __name__ == '__main__':
  a = int(input("Enter a: "))
  b = int(input("Enter b: "))
  makes10(a, b)