# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n = int(input('Enter numbers of keys: '))

my_dict = {i: {input('enter name: '): input('enter email: ')} for i in range(n+1)}
print(my_dict)
