# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)



def need_email(dict_):
    for data in dict_.values():
        if 'email' not in data or not data['email']:
            print(data['name'])


my_dict = {
    'id1': {'name': 'Dima', 'surname': 'Zinevich', 'phone': '123', 'email': 'sad@a.ru'},
    'id2': {'name': 'Vlad', 'surname': 'Zinevich', 'phone': '123'},
    'id3': {'name': 'Vika', 'surname': 'Zinevich', 'phone': '123', 'email': ''}
}

need_email(my_dict)
