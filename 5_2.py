# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число


while True:
    try:
        first_decimal = float(input('enter first decimal: '))
        break
    except ValueError:
        print('enter valid decimal')

while True:
    action = input('enter action[/*-+]: ')
    if action not in '/*-+':
        print('wrong action')
        continue
    break

while True:
    try:
        second_decimal = float(input('enter second decimal: '))
        break
    except ValueError:
        print('enter valid decimal')

if action == '/':
    print(first_decimal/second_decimal)
elif action == '*':
    print(first_decimal*second_decimal)
elif action == '-':
    print(first_decimal-second_decimal)
else:
    print(first_decimal+second_decimal)


# second way
print(eval(f'{first_decimal}{action}{second_decimal}'))