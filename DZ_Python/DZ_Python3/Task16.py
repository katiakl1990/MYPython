#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. 
#Последняя строка содержит число X

#*Пример:*
#5
#    1 2 3 4 5
#    3
#   -> 1

import random

N = int(input('Введите кол-во элементов в массиве: '))
X = int(input('Введите число X: '))
list = []

for i in range(N):
    list.append(random.randint(1, N))
print(list) 

sum = 0 
for i in list:
    if i == X:
         sum += 1
print(f'{X} встречается {sum} раз')