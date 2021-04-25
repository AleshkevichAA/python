# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

script_name, hours_param, value_in_hour_param, bonus = argv
print('Имя скрипта: ', script_name)
print('Выработка в часах: ', hours_param)
print('Ставка в час: ', value_in_hour_param)
print('Премия: ', bonus)
result = int(hours_param) * float(value_in_hour_param) + float(bonus)
print(f'Итоговая сумма: {result}')
