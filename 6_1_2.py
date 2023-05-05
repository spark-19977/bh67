# 2. Написать функцию-генератор, принимающая целое число count, и возвращающая указанное колличество
# простых чисел:
# count=5
# result=2, 3, 5, 7, 11


def is_simple(number):
    delitel = number - 1
    while delitel > 1:
        if not number % delitel:
            return False
        delitel -= 1
    return True


def get_simple(count):
    start = 2
    for i in range(count):
        while not is_simple(start):
            start += 1
        yield start
        start += 1


print(a := [*get_simple(25)])
