import math

# a. Максимум из двух чисел
# a = int(input())
# b = int(input())
#
# if a >= b:
#     print(a)
# else:
#     print(b)

# b. Високосный год
# year = int(input("Enter a year: "))
#
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")

# c. Тестирующая система

# d. Знак числа
# def sin(x):
#     if x > 0:
#         return 1
#     elif x < 0:
#         return -1
#     else:
#         return 0
#
# x = int(input())
#
# print(sin(x))

#e Какое из чисел больше?
def compare(x, y):
    if x > y:
        return 1
    elif x < y:
        return 2
    else:
        return 0

x = int(input("Enter num1: "))
y = int(input("Enter num2: "))

print(compare(x, y))

