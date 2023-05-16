# . Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None
class Car:
    def __init__(self, color:str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return (f'Car({self.color} color, {self.count_passenger_seats} passengers seats,' 
                f'{"" if self.is_baby_seat else "dont"} have baby seat, '
                f'{"" if self.is_busy else "dont"} busy)')

class Taxi:
    def __init__(self, cars: list[Car]):
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool):
        for car in self.cars:
            if not car.is_busy and count_passengers <= car.count_passenger_seats and ( not is_baby or car.is_baby_seat):
                car.is_busy = True
                return car


taxi = Taxi([Car('yellow', 3, True),Car('pink', 6, False)])
print(taxi.find_car(6, True))
print(taxi.find_car(6, False))
