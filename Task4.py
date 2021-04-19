# 4. Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
#
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car():
    speed = ''
    color = ''
    name = ''

    direction_list = ['Left', 'Right']

    def __init__(self, speed, color, name, is_police='False'):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Поехала!')

    def stop(self):
        print('Остановились')

    def turn(self, direction):
        print('Повернула ', direction)

    def show_speed(self):
        print('Speed: ', self.name, ' - ', self.speed)


class TownCar(Car):
    def show_speed(self):
        if (float(self.speed) > 60):
            print(f'Towncar increase speed limit {self.speed}>60 !!!')
        else:
            print('Speed:', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if (float(self.speed) > 40):
            print(f'Workcar increase speed limit {self.speed}>40 !!!')
        else:
            print('Speed:', self.speed)


class PoliceCar(Car):
    pass


# , SportCar, WorkCar, PoliceCar

towncar = TownCar(70, 'white', 'Lincoln')
print('Towncar:', towncar.name, ', color:', towncar.color, ', speed:', towncar.speed,
      ', Police' if towncar.is_police == True else ', Not Police')
towncar.show_speed()

sportcar = SportCar(200, 'Imola Red', 'Ferrari')
print('SportCar:', sportcar.name, ', color:', sportcar.color, ', speed:', sportcar.speed,
      ', Police' if sportcar.is_police == True else ', Not Police')
sportcar.show_speed()

workcar = WorkCar(41, 'Grey', 'Dodge')
print('WorkCar:', workcar.name, ', color:', workcar.color, ', speed:', workcar.speed,
      ', Police' if workcar.is_police == True else ', Not Police')
workcar.show_speed()

policecar = PoliceCar(80, 'white-blue', 'Ford', True)
print('PoliceCar:', policecar.name, ', color:', policecar.color, ', speed:', policecar.speed,
      ', Police' if policecar.is_police == True else ', Not Police')
policecar.show_speed()
