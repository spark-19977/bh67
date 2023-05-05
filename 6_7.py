# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка


def neighbor(list_: list):
    for i in range(len(list_)):
        yield list_[i], sum((list_[i - 1], list_[i + 1] if i+1 < len(list_) else list_[0]))


list_ = [1, 4, 345, 346, 56, 2, 567, 7, 3]
print({k: v for k, v in neighbor(list_)})
