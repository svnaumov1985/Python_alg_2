# Определить, какое число в массиве встречается чаще всего.

import random

MAX = 10

mas = [random.randint(0, MAX) for i in range(random.randint(5, MAX))]

dict = {}
max_count = 0
value = 0

for i in mas:


    dict[i] = 1 if dict.get(i) == None else dict[i] + 1
    if dict[i] > max_count:
        value = i

print(mas)
print(value)
