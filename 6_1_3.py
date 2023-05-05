# 3. Написать рекурсивную функцию, принимающая строку, и разворачивающая ее задом на перед


def reverse_(string):
    if not string:
        return ''
    return string[-1] + reverse_(string[:-1])


print(reverse_('123456789'))
