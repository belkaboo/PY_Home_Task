# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

n = int(input('Введите кол-во кустов: '))
shrub_list= [randint(1,20) for i in range(n)]
print(shrub_list)
harvest_list = []

for i in range(len(shrub_list) - 1):
    harvest_list.append(shrub_list[i - 1] + shrub_list[i] + shrub_list[i + 1])
harvest_list.append(shrub_list[-2] + shrub_list[len(shrub_list) - 1] + shrub_list[0]) 

print(harvest_list)
print(max(harvest_list))