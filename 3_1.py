# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

def text_replace1(text):
    return text.replace(' ', '-')


def text_replace2(text):
    return text.translate(str.maketrans(' ', '-'))


def text_replace3(text):
    result = ''
    for symbol in text:
        if symbol != ' ':
            result += symbol
        else:
            result += '-'
    return result


text = input('Enter sentence: ')
text1 = text_replace1(text)
text2 = text_replace2(text)
text3 = text_replace3(text)
print('Sentence replaced in first way:')
print(text1)
print('=' * 30)
print('Sentence replaced in second way:')
print(text2)
print('=' * 30)
print('Sentence replaced in third way:')
print(text3)
