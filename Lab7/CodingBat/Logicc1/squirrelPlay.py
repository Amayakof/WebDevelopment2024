import random
# The squirrels in Palo Alto spend most of the day playing.
# In particular, they play if the temperature is between 60 and 90 (inclusive).
# Unless it is summer, then the upper limit is 100 instead of 90.
# Given an int temperature and a boolean is_summer, 
# return True if the squirrels play and False otherwise.

# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True

def squirrel_play(temp, is_summer):
    if is_summer:
        return temp >= 60 and temp <= 100
    return temp >= 60  and temp <= 90


if __name__ == '__main__':
    temp = random.randint(0, 100)
    if temp >= 80:
        is_summer = random.choice([True, False])
    else:
        is_summer = False
    print(f"Temperature is: {temp}, is it summer? {is_summer}")
    print(squirrel_play(temp, is_summer))
