# Задача 32: Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше 
# заданного максимума)

n = int(input('Введите размер массива: '))
some_list = [random.randint(1,40) for _ in range(n)]
print(some_list)

x = int(input('Введите диапазон от: '))
y = int(input('Введите диапазон до: '))
print(some_list[x:y+1])