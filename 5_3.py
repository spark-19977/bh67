# **Вывести четные числа от 2 до N по 5 в строку


while True:
    try:
        n = float(input('enter N: '))
        break
    except ValueError:
        print('enter valid decimal')

decimal = 2
i = 1
while decimal <= n:
    print(decimal, end=' ' if i % 5 else '\n')
    i += 1
    decimal += 2
