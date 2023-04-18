# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

first_number = float(input(f'Enter first number: '))
second_number = float(input(f'Enter second number: '))
third_number = float(input(f'Enter third number: '))

positive = 0
negative = 0

if first_number > 0:
    positive += 1
elif first_number < 0:
    negative += 1
if second_number > 0:
    positive += 1
elif second_number < 0:
    negative += 1
if third_number > 0:
    positive += 1
elif third_number < 0:
    negative += 1
print(f'You entered {positive} positive numbers and {negative} negative')
