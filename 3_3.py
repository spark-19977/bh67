# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами


def get_int(name='number'):
    while True:
        try:
            number = int(input(f'Enter {name}: '))
            return number
        except ValueError:
            print(f"Please enter valid {name}")


name = input('Enter your name: ')
age = get_int('age')
city = input('Enter city you live: ')

print('First way:')
print(f'Hello {name}({age} years) from {city}')
print('=' * 30)
print('Second way:')
print('Hello {name}({age} years) from {city}'.format(name=name, age=age, city=city))
print('=' * 30)
print('Third way:')
print('Hello {0}({1} years) from {2}'.format(name, age, city))
