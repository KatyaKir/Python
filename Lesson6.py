# Задача №1
from time import sleep

class TrafficLight:
    __color = None
    def out_color(self):
        while True:
            print("\033[31m {}".format('[•]'))
            sleep(7)
            print("\033[33m {}".format('[•]'))
            sleep(2)
            print("\033[32m {}".format('[•]'))
            sleep(7)
            print("\033[33m {}".format('[•]'))
            sleep(2)

svet = TrafficLight()
svet.out_color()


# Задача №2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asfalt(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return "На дорогу длиной %d м и шириной %d м необходимо %d тонн асфальта" % (self._length, self._width, mass)

road_ = Road(int(input('Длина дороги в метрах:')), int(input('Ширина дороги в метрах:')))
print(road_.asfalt())


# Задача №3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return  full_name

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


worker_ = Position(input('Введите имя сотрудника:'), input('Введите фамилию сотрудника:'), input('Введите должность сотрудника:'), int(input('Введите з/п сотрудника:')), int(input('Введите бонус сотрудника:')))
print(worker_.get_full_name())
print(worker_.position)
print(worker_.get_total_income())


# Задача №4


# Задача №5

