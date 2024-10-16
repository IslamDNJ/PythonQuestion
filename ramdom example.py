import random

# Заполнение массива случайными целыми числами
array = [random.randint(1, 1000) for _ in range(1000)]

# Переменная для хранения количества пар и максимальной суммы
pair_count = 0
max_pair_sum = 0

# Поиск пар
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if (array[i] % 5 == 0 or array[j] % 5 == 0) and (array[i] % 2 == 0 or array[j] % 2 == 0):
            pair_count += 1
            pair_sum = array[i] + array[j]
            if pair_sum > max_pair_sum:
                max_pair_sum = pair_sum

print("Количество пар, удовлетворяющих условиям:", pair_count)
print("Наибольшая сумма элементов пары:", max_pair_sum)
