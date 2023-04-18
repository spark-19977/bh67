# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3


def get_float(message='Enter number: '):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Please enter valid number")


first_number = get_float()
second_number = get_float()
third_number = get_float()
average = round(sum((first_number, second_number, third_number))/3,3)
print(average)
