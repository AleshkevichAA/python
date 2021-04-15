#  Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

def finder_func(file_name):
    sum_zp = 0
    sotr = 0
    try:
        with open(file_name, 'r', encoding='UTF-8') as f_obj:
            lines = f_obj.read()
            print('Сотрудники с зарплатой менее 20000 руб:')
            for line in lines.split('\n'):
                line = line.split(' ')
                sum_zp += float(line[1])
                sotr += 1
                if (float(line[1]) < 20000):
                    print(line[0])
    except IOError:
        print("Произошла ошибка ввода-вывода!")
    print('Средняя зарплата = {:.2f}'.format(sum_zp / sotr))


file_name = input('Введите имя файла для анализа:')
finder_func(file_name)
