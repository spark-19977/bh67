# 1. Написать функцию-генератор, принимающую 3 аргумента (number, start, end), все аргументы целочисленные
# Генератор должен возвращать number в степени от start до end:
# number=2
# start=3
# end=5
# result: 8, 16, 32


def get_square_numbers(number, start, end):
    for i in range(start, end + 1):
        yield pow(number, i)


number = 2
start = 3
end = 5

print([*get_square_numbers(number, start, end)])
