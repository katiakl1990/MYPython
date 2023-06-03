#  Задание 44 

# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() 

import pandas as pd

lst1 = []
lst2 = []
for i in range(len(lst)):
  if lst[i] == 'human':
    lst1.append(int(1))
    lst2.append(int(0))
  else:
    lst1.append(int(0))
    lst2.append(int(1))

data2 = pd.DataFrame({'whoAmI': lst, 'human': lst1, 'robot': lst2})
data2
