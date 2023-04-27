# Вывести первые N цисел кратные M и больше K
import math


while True:
    try:
        n = int(input('enter integer N: '))
        break
    except ValueError:
        print('enter valid integer')

while True:
    try:
        m = int(input('enter integer M: '))
        if not m:
            print('M cannot be zero')
            continue
        break
    except ValueError:
        print('enter valid integer')

while True:
    try:
        k = float(input('enter decimal K: '))
        k += 1
        k = math.floor(k)
        break
    except ValueError:
        print('enter valid decimal')

while k % m:
    k += 1

for i in range(n):
    print(k)
    k += m
