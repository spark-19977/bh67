# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3

first_number = float(input(f'Enter first number: '))
second_number = float(input(f'Enter second number: '))
third_number = float(input(f'Enter third number: '))
average = round(sum((first_number, second_number, third_number)) / 3, 3)
print(average)
