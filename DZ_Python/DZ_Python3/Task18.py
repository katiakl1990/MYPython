#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному 
#числу X. Пользователь в первой строке вводит натуральное число N – количество элементов 
#в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

#*Пример:*
#5
#    1 2 3 4 5
#    6
#   -> 5

import random

N = int(input('Введите кол-во элементов в массиве: '))
X = int(input('Введите число X: '))
list = []

for i in range(N):
     list.append(random.randint(1, N))
print(list) 

element = list[0]
elementX = abs(list[0] - X)

for i in list:
    if abs(i - X) < elementX and X != i:
        elementX = abs(i - X) 
        element = i

print(element)