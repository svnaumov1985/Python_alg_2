# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

dict = {i:0 for i in range(2,10)}

for i in range(2, 100):
    for a in range(2, 10):
        dict[a] += 1 if i % a == 0 else 0

for a in dict:

    print(a, " - ", dict[a])