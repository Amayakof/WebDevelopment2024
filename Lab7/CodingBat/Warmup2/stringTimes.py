# Given a string and a non-negative int n,
# return a larger string
# that is n copies of the original string.

def string_times(str, n):
  new_str = ""
  for i in range(n):
    new_str += str
  return new_str


if __name__ == '__main__':
    str = "Hello"
    n = 2
    print(string_times(str, n))
