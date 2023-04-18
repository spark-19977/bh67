# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами


name = input('Enter your name: ')
age = int(input(f'Enter your age: '))
city = input('Enter city you live: ')

print('First way:')
print(f'Hello {name}({age} years) from {city}')
print('=' * 30)
print('Second way:')
print('Hello {name}({age} years) from {city}'.format(name=name, age=age, city=city))
print('=' * 30)
print('Third way:')
print('Hello {0}({1} years) from {2}'.format(name, age, city))
