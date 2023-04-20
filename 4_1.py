# Заполнить список степенями числа 2 (от 2^1 до 2^n).

n = int(input('Enter exponent of 2: '))

exponent_list = [2**(i+1) for i in range(n)]
print(exponent_list)