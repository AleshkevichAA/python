# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @abstractmethod
    def get_value_textile(self):
        return f'Результат расчёта'


# Костюм
class Suit(Clothes):
    res = 0

    @property
    def get_result(self):
        return f'{self.res}'

    def get_value_textile(self):
        self.res = int(2 * (float(self.height/100)) + 0.3)


# Пальто
class Coat(Clothes):
    res = 0

    @property
    def get_result(self):
        return f'{self.res}'

    def get_value_textile(self):
        self.res = int((self.size / 6.5) + 0.5)


suit = Suit(56, 180)
suit.get_value_textile()
print(f'Ткани на пальто необходимо  {suit.get_result}')

coat = Coat(56, 180)
coat.get_value_textile()
print(f'Ткани на костюм необходимо {coat.get_result}')
