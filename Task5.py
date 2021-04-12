#  Реализовать формирование списка, используя функцию range() и возможности генератора.
#  В список должны войти четные числа от 100 до 1000 (включая границы).
#  Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def generate_spisok():
    return [el for el in range(100, 1001) if el % 2 == 0]


def find_multiplying(prev_el, el):
    return prev_el * el


even_list = generate_spisok()
print(even_list)
print('Результат вычисления:', reduce(find_multiplying, even_list))
