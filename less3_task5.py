# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

MAX = 10

mas = [random.randint(0, MAX) for i in range(random.randint(5, MAX))]

dict = [{"ind": i, "val": val} for i, val in enumerate(mas)]

need_do = True
while need_do:
    need_do = False
    for i in range(len(dict) - 1):
        if dict[i]["val"] > dict[i+1]["val"]:
            dict[i], dict[i+1] = dict[i+1], dict[i]
            need_do = True

print(mas)
print("Наименьшие значения: ")
print(dict[0])
print(dict[1])