# Подсчитать среднее арифметическое N чисел, вводимых с клавиатуры


while True:
    try:
        n = int(input('enter integer N: '))
        break
    except ValueError:
        print('enter valid integer')

sum_ = 0
for i in range(n):
    while True:
        try:
            number = float(input('enter number: '))
            break
        except ValueError:
            print('enter valid number')
    sum_ += number

print(sum_/n)
