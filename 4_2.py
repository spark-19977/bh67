# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

text = input('Enter text: ')
letter_dict = {k: text.count(k) for k in set(text)}
print(letter_dict)
