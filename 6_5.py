# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

def my_reverse(list_: list):
    for i in range(-1, -len(list_)-1, -1):
        yield list_[i]


list_ = [1, 2, 3, 5, 3, 456, 46, 7]
print([*my_reverse(list_)])
