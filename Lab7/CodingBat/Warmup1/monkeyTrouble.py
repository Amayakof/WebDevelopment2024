#We have two monkeys, a and b,
# and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling
# or if neither of them is smiling.
# Return True if we are in trouble.
def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


if __name__ == '__main__':
    a_smile = input("Is Monkey a Smiling? (True/False): ").lower()
    b_smile = input("Is Monkey b Smiling? (True/False): ").lower()
    a_smile = a_smile == "true" #turning them to bool using the comparisons
    b_smile = b_smile == "true"
    print(monkey_trouble(a_smile, b_smile))
