# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные


list_ = [1, 4, 345, 346, 56, 2, 567, 8, 1]
print([*filter(lambda x: not x % 2, sorted(list_)), *filter(lambda x: x % 2, sorted(list_))])
