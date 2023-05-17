# Написать класс ConfigParser
# конструктор класса принимает строковый аргумент в виде
# text = '''
# [Section1]
# key1=value1
# key2=value2
#
# [Section2]
# key3=value3
# key4=value4
# key5=value5
# '''
#
# 1. Написать метод объекта dict, приводящий эту строку к словарю вида
# {
# 	'Section1':
# 		{'key1': 'value1', 'key2': 'value2'},
#    	'Section2':
#   		{'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}
# }
#
# 2. Написать метод объекта get приминающий имя секции и ключ и возвращающий
#  значение, если нет такой секции или ключа в указанной секции, то вызвать
#  исключение ValueError
#
# 3. Написать метод объекта add_section принимающий имя новой секции и создающий
#  ее, если такая секция есть, вызывать исключение ValueError
#
# 4. Написать метод объекта add_param приминающий имя секции,
#  имя нового ключа и его значение, и создающий
#  новый ключ со значение в указанной секции
#  в случае если нет секции - исключение
#  в случае если в секции уже есть такой параметр, изменить его значение
#  на новое
#
# 5. Написать метод объекста has_section принимающий имя секции и возвращающий True
#  если такая секция есть, False в противном случае
#
# 6. Написать метод объекта has_param принимающий имя секции и имя параметра и возвращающий True
# если есть такой параметр в указанной секции, False в противном случае
# Если секции переданной на вход данного метода не существует, вызвать исключение ValueError
#
# 7. Написать метод объекта del_section принимающий имя секции и удаляющий секцию и все ее параметры
# Если такой секции нет, ничего не должно происходить
#
# 8. Написать метод объекта del_param принимающий имя секции и имя параметра и удаляющий данный параметр в
# указанной секции, если такого параметра в указанной секции или такой секции нет, то ничего не должно происходить
#
# 9. Написать магический метод __str__ приводящий вышеуказанный словарь обратно к строке согласно шаблону





class ConfigParser:
    def __init__(self, text: str):
        self.text = text

    def dict(self):
        i = 0
        result = {}
        while '[' in self.text[i:]:
            start = self.text.index('[', i)
            end_key = self.text.index(']', i)
            end = (self.text.index('[', start + 1)) if ('[' in self.text[start + 1:]) else len(self.text)
            key = self.text[start + 1:end_key]
            inside_dict = {}
            for string in self.text[end_key + 1:end].strip().split('\n'):
                if '=' in string:
                    ikey, ival = string.split('=')
                    inside_dict[ikey] = ival
            result[key] = inside_dict
            i = end
        return result

    def get(self, section_name, key):
        try:
            return self.dict()[section_name][key]
        except KeyError as err:
            raise ValueError(err)

    def add_section(self, new_section):
        if new_section in self.dict():
            raise ValueError
        self.text += f'\n[{new_section}]\n'
        return self.text

    def add_param(self, section, new_key, new_value):
        if section not in self.dict():
            raise ValueError
        section_start = self.text.index(section) + len(section) + 1
        section_end = (self.text.index('[', section_start) - 1) if '[' in self.text[section_start:] else len(self.text)
        new_dict = self.dict()[section]
        new_dict[new_key] = new_value
        new_text_fragment = '\n'
        for k, v in new_dict.items():
            new_text_fragment += f'{k}={v}\n'
        self.text = self.text[:section_start] + new_text_fragment + self.text[section_end:]

    def has_section(self, section):
        return section in self.dict()

    def has_param(self, section, param):
        try:
            return param in self.dict()[section]
        except KeyError as err:
            raise ValueError(err)

    def del_section(self, section):
        try:
            start_section = self.text.index(section)
            end_section = (self.text.index('[', start_section) - 1) if '[' in self.text[start_section:] else len(
                self.text)
            self.text = self.text[:start_section-2] + self.text[end_section:]
        except ValueError:
            pass

    def del_param(self, section, param):
        try:
            value = self.dict()[section][param]
            start_section = self.text.index(section)
            end_section = (self.text.index('[', start_section) - 1) if '[' in self.text[start_section:] else len(
                self.text)
            self.text = (self.text[:start_section] +
                         self.text[start_section:end_section].replace(f'{param}={value}\n', '') +
                         self.text[end_section:]
                         )
        except ValueError: ...
        except KeyError: ...

    def __str__(self):
        result = ''
        for k, v in self.dict().items():
            result += f'[{k}]\n'
            for ik, iv in v.items():
                result += f'{ik}={iv}\n'
            result += '\n'
        return result.strip()


text = '''
[Section1]
key1=value1
key2=value2

[Section2]
key3=value3
key4=value4
key5=value5

[assa]
'''
a = ConfigParser(text)
a.del_param('Section1', 'key1')
# print(a.add_section('ssaa'))
# print(a.dict())
# print(a.text)

# a.del_section('Section2')
print(a.dict())
print(a)
# print(a.dict())
