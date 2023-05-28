# Задача 42: Узнать какая максимальная households в зоне минимального значения population

print(f'Макс. households при мин. population: {df.loc[df.population < df.population.quantile(.15)].households.max()}')