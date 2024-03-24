import math

# a. Минимум 4 чисел
# def min_number(a, b, c, d):
#     return min(a, b, c, d)
#
#
# a, b, c, d = map(int, input("Enter 4 numbers divided by Space: ").split())
# print("The smallest number: ", min_number(a, b, c, d))

# b. Степень
# def double_power(a, n):
#     return a**n
#
#
# a = float(input("Enter a number: "))
# n = int(input("Enter a power: "))
# print("The power: ", double_power(a, n))

# c. Исключающее ИЛИ
def xor(x, y):
    return (x or y) and not (x and y)


x, y = map(int, input("Enter two numbers divided by Space: ").split())
print("XOR Result: ", int(xor(x, y)))