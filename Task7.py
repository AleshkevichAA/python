#  7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json


def writer_json(data, file_name='my_file.json'):
    """
    :param data: данные
    :param file_name: имя файла, для сохранения данных в формате json
    :return:
    """
    with open(file_name, "w") as write_f:
        json.dump(data, write_f)


def reader_json(file_name='my_file.json'):
    """
    :param file_name: имя файла, для чтения данных в формате json
    :return:
    """
    with open(file_name, "r") as reader_f:
        print('Итоговый словарь: ', file_name)
        print(json.load(reader_f))


def get_list(file_in='data7.txt'):
    """
    Получение списка данных
    :param file_name: исходный файл
    :return: список
    """
    with open(file_in, 'r', encoding='UTF-8') as f_obj:
        data_list = []
        firm_dict = {}
        sum_profit = 0
        profit_counter = 0
        print('Исходный файл : ', file_in)
        while True:
            line = f_obj.readline()
            print(line.replace('\n', ''))
            if line == '':
                break
            lines = line.split(' ')
            balans = int(lines[2]) - int(lines[3])
            if (balans > 0):
                profit_counter += 1
                sum_profit += balans
            firm_dict.update({lines[0]: balans})
        data_list.append(firm_dict)
        data_list.append({'average_profit': int(sum_profit / profit_counter)})
        return data_list


writer_json(get_list())

reader_json()
