# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите сторое число: '))

def sum_of_nums(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b       
    else:
        return sum_of_nums(a + 1, b - 1)

print(sum_of_nums(num_1,num_2))
