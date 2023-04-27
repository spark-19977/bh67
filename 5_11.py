# Вводится число, найти его максимальную цифру


while True:
    number = input('enter number: ')
    try:
        float(number)
        break
    except ValueError:
        print('enter valid number')


max_ = 0
for i in number:
    if i in '+-.':
        continue
    i = int(i)
    if i > max_:
        max_ = i

print(max_)
