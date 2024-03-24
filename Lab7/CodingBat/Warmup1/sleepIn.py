# The parameter weekday is True if
# it is a weekday,
# and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation.
# Return True if we sleep in.
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

if __name__ == '__main__':
  weekday = input("Is it a weekday? (y/n): ")
  weekday = weekday.lower() == 'y'

  vacation = input("Is it a vacation? (y/n): ")
  vacation = vacation.lower() == 'y'

  print("Do we sleep in? ", sleep_in(weekday, vacation))

