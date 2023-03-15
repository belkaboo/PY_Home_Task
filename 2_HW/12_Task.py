# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

from random import randint

x = randint(0,1000)
y = randint(0,1000)
sum, prod = x + y , x * y

print('Петя загадал 2 числа, сумма этих чисел - {} , произведение - {}\n'.format(sum,prod))

flag = False
for i in range(1001):
    for j in range(1001):
        if i + j == sum and i * j == prod:
            print('{} и {}'.format(i,j))
            flag = True           
            break
    if flag:
        break
