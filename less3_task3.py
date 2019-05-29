#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

MAX = 10

mas = [random.randint(0, MAX) for i in range(random.randint(5, MAX))]

dict = {"min": {"val": MAX+1, "index": 0}, "max": {"val": 0, "index": 0}}

print(mas)

for i, val in enumerate(mas):

    if val < dict["min"]["val"]:
        dict["min"]["val"], dict["min"]["index"] = val, i

    if val > dict["max"]["val"]:
        dict["max"]["val"], dict["max"]["index"] = val, i

mas[dict["min"]["index"]], mas[dict["max"]["index"]] = dict["max"]["val"], dict["min"]["val"]

print(mas)