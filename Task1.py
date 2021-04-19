# 1. Создать класс TrafficLight (светофор).
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight():
    __color_list = ['Red', 'Yellow', 'Green']
    __color = 'Red'

    def running(self):
        # переключение в цвета
        while True:
            if (self.__color == self.__color_list[0]):
                print('Red')
                self.__color = self.__color_list[1]
                time.sleep(7)
            elif (self.__color == self.__color_list[1]):
                print('Yellow')
                self.__color = self.__color_list[2]
                time.sleep(2)
            elif (self.__color == self.__color_list[2]):
                print('Green')
                self.__color = self.__color_list[0]
                time.sleep(5)
            else:
                print('Непонятное состояние')


a = TrafficLight()
a.running()
