#   Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
# были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

file_in = 'data6.txt'


def get_hours(stroka):
    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    res = ''
    for i in stroka:
        if i in digits:
            res += i
        else:
            break
    return res


dict = {}
def taks6():
    with open(file_in, 'r', encoding='UTF-8') as f_obj:
        while True:
            line = f_obj.readline()
            print(line.replace('\n', ''))
            if line == '':
                break
            # предмет
            key_dict = line[:line.index(':')]
            # подсчёт часов
            lines = (line[(line.index(':') + 1):]).split(' ')
            sum = 0
            for el in lines:
                el = get_hours(el)
                if (el.isnumeric()):
                    sum += int(el)
            dict.update({key_dict: sum})
    print('Новый словарь: ', dict)

taks6()