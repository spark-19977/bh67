# Написать класс Card
#  1. Конструктор класса объявляет атрибут объекта __card_number со значением None, атрибут _discount со значением 5
#  2. Описать property и setter для атрибута _discount, property должен возвращать значение, setter должен
# проверять новое значение на тип int, а так же что новое значение >= 1 и присваивать новое значение атрибуту,
# если оно удовлетворяет условиям, в противном случае должно вызываться соответствующее исключение с текстом
#  3. Написать  property для атрибута __card_number возвращающий значение атрибута
# Написать класс CardCreater
#  1. Атрибут класса card являющийся списком
#  2. Метод класса create принимающий колличество, и создающий экземпляры класса Card, все созданные карты
# необходимо складывать в атрибут класса card, а так же каждой карте необходимо выдавать значение атрибута
# __card_number, значение должно быть уникальным среди всех экземпляров в списке card
import random


class Card:
    def __init__(self, card_number: int = None, discount: int = 5):
        if card_number is None:
            self.__card_number = random.randint(10000000,99999999)
        else:
            self.__card_number = card_number
        self._discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, new_value):
        if not isinstance(new_value, int):
            raise TypeError('new discount value must be integer')
        if new_value < 1:
            raise ValueError('new discount value must be not lower then 1')
        self._discount = new_value

    @property
    def card_number(self):
        return self.__card_number


class CardCreator:
    cards = []
    cards_numbers = []

    @classmethod
    def create(cls, amount):
        for i in range(amount):
            card_number = random.randint(10000000, 99999999)
            while card_number in cls.cards_numbers:
                card_number = random.randint(10000000, 99999999)
            cls.cards_numbers.append(card_number)
            cls.cards.append(Card(card_number))


CardCreator.create(10)
print(CardCreator.cards)
print(CardCreator.cards_numbers)
