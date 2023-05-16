# . Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категор


class Category:
    categories = []

    @classmethod
    def add(cls, category):
        if category in cls.categories:
            raise ValueError
        cls.categories.append(category)
        return len(cls.categories) - 1

    @classmethod
    def get(cls, index):
        return cls.categories[index]

    @classmethod
    def delete(cls, index):
        if index < len(cls.categories):
            del cls.categories[index]

    @classmethod
    def update(cls, index, new_name):
        if new_name in cls.categories:
            raise ValueError
        if index < len(cls.categories):
            cls.categories[index] = new_name
        else:
            cls.add(new_name)