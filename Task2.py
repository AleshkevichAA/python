# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123]
from random import randint


def generate_func(max_count=12, max_element=300):
    my_list = [randint(1, max_element) for i in range(0,max_count)]
    print(my_list)
    new_list = [second_el for first_el, second_el in zip(my_list, my_list[1:]) if second_el > first_el]
    return new_list


print('Итоговое множество', generate_func(int(input('Максимальное количество элементов списка: ')),
                                          int(input('Введите максимальное значение элемента: '))))
