# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int


def bin_int_converter(decimal):
    if isinstance(decimal, str):
        if not decimal.startswith('0b'):
            raise TypeError(f'Invalid bin number: {decimal}')
        if decimal.endswith('0b'):
            return 0
        return bin_int_converter(decimal[:-1]) * 2 + (1 if decimal[-1] == '1' else 0)
    elif isinstance(decimal, int):
        if not decimal:
            return '0b0'
        elif decimal == 1:
            return '0b1'
        int_, waste = divmod(decimal, 2)
        return bin_int_converter(int_) + f'{waste}'

def bin_int_converter2(decimal):
    if isinstance(decimal, int):
        result = []
        if not decimal:
            return '0b0'
        while decimal:
            decimal, waste = divmod(decimal, 2)
            result.append(str(waste))
        return f'0b{"".join(reversed(result))}'
    elif isinstance(decimal, str):
        if not decimal.startswith('0b'):
            raise TypeError(f'Invalid bin number: {decimal}')
        result = 0
        decimal=decimal[2:]
        while decimal:
            result = result * 2 + (1 if decimal[0]=='1' else 0)
            decimal = decimal[1:]
        return result
n = 101
print(n)
print(bin_int_converter(n))
print(bin_int_converter(bin_int_converter(n)))
print(n)
print(bin_int_converter2(n))
print(bin_int_converter2(bin_int_converter2(n)))
