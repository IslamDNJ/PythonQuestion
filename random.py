import random

# Задаем диапазон
lower_bound = 20
upper_bound = 100

# Заполняем массив
array = [random.randint(lower_bound, upper_bound) for _ in range(20)]

# Выводим массив
print(array)

import random

# Заполнение массива случайными целыми числами из диапазона 20:100
my_array = [random.randint(20, 100) for _ in range(20)]

# Вывод на экран всех элементов массива
print("Массив:", my_array)

# Вывод на экран элементов, кратных 3, и их количество
multiples_of_3 = [num for num in my_array if num % 3 == 0]
print("Элементы, кратные 3:", multiples_of_3)
print("Количество элементов, кратных 3:", len(multiples_of_3))

