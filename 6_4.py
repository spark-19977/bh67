# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно


list_ = [12, '12', 'asd',{12}]
print([*filter(lambda x: isinstance(x, str), list_)])
