#Given 2 int values,
# return True if one is negative and one is positive.
# Except if the parameter "negative" is True,
# then return True only if both are negative.

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

if __name__ == '__main__':
  a = int(input("Enter number A: "))
  b = int(input("Enter number B: "))
  negative = input("Is negative? (True/False) ").lower()
  negative = negative == 'true'
  print(pos_neg(a, b, negative))