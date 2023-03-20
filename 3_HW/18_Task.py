# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

num = int(input('Введите кол-во элементов массива: '))
x = int(input('Введите число X: '))

list_nums = [randint(1,50) for i in range(num)]
res_index, diff = 0, abs(list_nums[0] - x)

for i in range(1, num):
    if abs(list_nums[i] - x) < diff:
        diff, res_index = abs(list_nums[i] - x), i
        
print(list_nums)
print('{} - ближайший элемент в массиве к числу {}' .format(list_nums[res_index],x))