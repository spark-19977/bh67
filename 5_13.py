# "Угадай число"
# from random import randint
# a = randint(1, 100)
# Данная функция генерирует случайное число в заданном диапазоне,
# необходимо написать игру "угадай число" и сказать сколько попыток ушло на
# это у пользователя


from random import randint
a = randint(1, 100)
i = 0
number = 0
while a != number:
    while True:
        try:
            number = int(input('enter integer in range from 1 to 100: '))
            break
        except ValueError:
            print('enter valid integer')
    i += 1

print(i)
