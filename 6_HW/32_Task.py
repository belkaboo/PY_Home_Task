# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

n_min = int(input('Введите нижнюю границу отсева: '))
n_max =int(input('Введите верхнюю границу отсева: '))

list_1 = [randint(-10,10) for i in range(5,10)]
print(type(list_1))
print(list_1)

for i in range(list_1.__len__()):
    if n_min <= list_1[i] <= n_max:
        print(i, sep:=' ', end= '')