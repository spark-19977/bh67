# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных


def get_float(name='number'):
    while True:
        try:
            number = float(input(f'Enter {name}: '))
            return number
        except ValueError:
            print(f"Please enter valid {name}")


my_numbers = []
for i in range(3):
    my_numbers.append(get_float())
positive = 0
negative = 0
for number in my_numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
print(f'you entered {positive} positive numbers and {negative} negative')
