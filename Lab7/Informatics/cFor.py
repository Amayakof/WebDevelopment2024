import math
# a. Четные числа
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
#
# for i in range(a, b+1):
#     if i % 2 == 0:
#         print(i, end=" ")

# b. Остаток
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# d = int(input("Enter d: "))
#
# for i in range(a, b+1):
#     if i % d == c:
#         print(i, end=" ")

# c. Квадраты
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# is_square = False
# for i in range(a, b+1):
#     if math.isqrt(i) ** 2 == i:
#         print(i, end=" ")
#         is_square = True

# d. Цифра в числе
# x = int(input("Enter x: "))
# d = int(input("Enter d: "))
# x_str = str(x)
# counter = 0
# for digit in x_str:
#     if int(digit) == d:
#         counter += 1
#
# print(counter)

# e. Сумма цифр
# x = int(input("Enter x: "))
# counter = 0
# x_str = str(x)
# for digit in x_str:
#     counter = counter + int(digit)
#
# print(counter)

# f. Переверни число
# x = int(input("Enter x: "))
# x_str = str(x)
# reversed_x = int(x_str[::-1])
# print(reversed_x)

# g. Минимальный делитель
# x = int(input("Enter x: "))
# for i in range(1, x+1):
#     if x % i == 0 and i != 1:
#         print(i)
#         break

# h. Делители числа
# x = int(input("Enter x: "))
# for i in range(1, x+1):
#     if x % i == 0:
#         print(i, end=" ")

# i. Количество делителей
# x = int(input("Enter x: "))
# counter = 0
# for i in range(1, x+1):
#     if x % i == 0:
#         counter +=1
#
# print(counter)

# j. Сумма ста
# sum = 0
# for _ in range(100):
#     number = int(input())
#     sum += number
# print(sum)

# k. Сумма чисел
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(n):
#     number = int(input(f"Number {i+1}: "))
#     sum += number
#
# print("Their sum: ", sum)

# l. Перевод числа
# binary_number = input("Enter a binary number: ")
# decimal_number = 0
#
# for i in range(len(binary_number)):
#     digit = int(binary_number[-(i+1)])
#     decimal_number += digit * (2 ** i)
#
# print("Decimal number: ", decimal_number)

# m. Нули
n = int(input("Enter a number: "))
counter = 0
for i in range(1, n+1):
    number = int(input(f"Enter a number {i}: "))
    if number == 0:
        counter += 1

print(counter)