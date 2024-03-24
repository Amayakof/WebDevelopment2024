# We have a loud talking parrot.
# The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking
# and the hour is before 7 or after 20.
# Return True if we are in trouble.
def parrot_trouble(talking, hour):
  if (talking and (hour < 7 or hour > 20)):
    return True


if __name__ == '__main__':
  talking = input("Is the parrot talking (True/False)").lower()
  hour = int(input("What hour is it? "))
  talking = talking == 'true'
  print(parrot_trouble(talking, hour))
