# 4**. Написать рукурсивную функцию, которая принимает целое число (depth), функция должна генерировать дерево указанной
# глубины, (каждая ветвь имеет 2 дочерних ветки):
# depth=3
# result=[[[], []], [[], []]]


def get_depth_tree(depth):
    if depth == 1:
        return []
    a = []
    a.append(get_depth_tree(depth-1))
    a.append(get_depth_tree(depth-1))
    return a


print(get_depth_tree(3))
