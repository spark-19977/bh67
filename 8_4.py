# . Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# IndexError


class Category:
    categories: list[dict[str, str | bool]] = []
    # [{name: aaa, is: bbb}, ]
    @classmethod
    def add(cls, category: str, is_published: bool):
        for categor in cls.categories:
            if category == categor['name']:
                raise ValueError
        cls.categories.append({'name': category, 'is_published': is_published})
        return len(cls.categories) - 1

    @classmethod
    def get(cls, index):
        return cls.categories[index]

    @classmethod
    def make_published(cls, index):
        cls.categories[index]['is_published'] =True

    @classmethod
    def make_unpublished(cls, index):
        cls.categories[index]['is_published'] =False

    @classmethod
    def delete(cls, index):
        if index < len(cls.categories):
            del cls.categories[index]

    @classmethod
    def update(cls, index, new_name, is_published):
        for category in cls.categories:
            if new_name == category['name']:
                raise ValueError
        if index < len(cls.categories):
            cls.categories[index] = {'name': new_name, 'is_published': is_published}
        else:
            cls.add(new_name, is_published)


a = Category()

a.add('asd',True)
print(a.categories)
# a.make_unpublished(2)
print(a.get(0))
print(a.categories)
a.update(2, 'asad', False)

print(a.categories)
