# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

text = input('Enter sentence: ')
text1 = text.replace(' ', '-')
text2 = text.translate(str.maketrans(' ', '-'))
text3 = '-'.join(text.split(' '))
print('Sentence replaced in first way:')
print(text1)
print('=' * 30)
print('Sentence replaced in second way:')
print(text2)
print('=' * 30)
print('Sentence replaced in third way:')
print(text3)
