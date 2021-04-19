#  Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker():
    name = ''
    surname = ''
    position = ''
    __dict__ = {}

    # {"wage": wage, "bonus": bonus}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__dict__ = {'wage': wage, 'bonus': bonus}

    def get_dict(self):
        return self.__dict__

    def set_dict(self, dict):
        self.__dict__ = dict


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        wage = float(self.get_dict().get('wage'))
        bonus = float(self.get_dict().get('bonus'))
        return wage + bonus


workers_list = [Position('Иван', 'Иванов', 'Рабочий', '10000', '20000'),
                Position('Петр', 'Петров', 'Рабочий', '15000', '15000'),
                Position('Тимофей', 'Сидоров', 'Бригадир', '20000', '20000'),
                Position('Фёдор', 'Цаплин', 'Ассистет бригадира', '12000', '20000')]

for i in workers_list:
    print(i.get_full_name(), ',доход с учётом премии:', int(i.get_total_income()), 'руб.')
