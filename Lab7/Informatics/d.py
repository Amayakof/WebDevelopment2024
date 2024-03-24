import math
# a. A[0], A[2], A[4], ...
# N = int(input("Enter a number: "))
# array = []
# for i in range(N):
#     element = int(input(f"Enter an element {i}: "))
#     array.append(element)
#
# for i in range(0, N, 2):
#     print(array[i], end=" ")

# b. Вывести четные элементы
# N = int(input("Enter a number: "))
# array = []
# for i in range(N):
#     element = input("Enter an element: ")
#     array.append(element)
#
# for i in range(N):
#     if int(array[i]) % 2 == 0:
#         print(array[i], end=" ")

# c. Количество положительных элементов
# N = int(input("Enter the number of elements: "))
# array = list(map(int, input("Enter the elements, divided by space: ").split()))
# counter = 0
# for num in array:
#     if num > 0:
#         counter += 1
#
# print(f"Number of Positive elements: ", counter)
# ex: 6
# 1 -1 2 6 4 3

# d. Количество элементов, больших предыдущего
# N = int(input("Enter the number of elements: "))
# array = list(map(int, input("Enter the elements, divided by space: ").split()))
# counter = 0
#
# for i in range(1, N):
#     if array[i] > array[i - 1]:
#         counter += 1
#
# print("Number of elements that sre greater than the previous one: ", counter)

# ex: 6
# 1 -1 2 6 4 3

# e. Есть ли два элемента с одинаковыми знаками
# N = int(input("Enter the number of elements: "))
# array = list(map(int, input("Enter the elements, divided by space: ").split()))
# similar_element = 0
# for i in range(1, N):
#     if array[i] * array[i-1] > 0:
#         similar_element = 1
#
# if similar_element:
#     print("YES")
#
# else:
#     print("NO")
#
# ex.: 3
# -1 2 2
#
# 5
# -1 1 -1 -1 1

# f. Количество элементов больших обоих соседей(строго большe)
# N = int(input("Enter the number of elements: "))
# array = list(map(int, input("Enter the elements, divided by space: ").split()))
# counter = 0
# #
# for i in range(1, N - 1):
#     if array[i] > array[i - 1] and array[i] > array[i + 1]:
#         counter += 1
# print(counter)
#
# ex.: 5
# 1 2 1 3 4

# g. Переставить элементы в обратном порядке
#Программа должна считать массив,
#поменять порядок его элементов, затем вывести результат

N = int(input("Enter the number of elements: "))
array = list(map(int, input("Enter the elements, divided by space: ").split()))

for i in range(N // 2):
    array[i], array[N - 1 - i] = array[N - 1 - i], array[i]

print("This is a Reversed Array:", array)
