import random
# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
n = int(input("Введите количество элементов списка: "))
list = []
for i in range(n):
    list.append(random.randint(-10, 10))
print(list)

min_num = int(input("Минимальный индекс: "))
max_num = int(input("Максимальный индекс: "))
for i in range(len(list)):
    if min_num <= list[i] <= max_num:
        print(i, end=" ")
