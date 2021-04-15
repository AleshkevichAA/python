# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.
file_name = 'data2.txt'


#  Тестовое заполнение файла
# try:
#     with open(file_name,'w') as f_obj:
#         f_obj.write('Введите строку, пустая строка конец ввода:\nпервая\nвторая\nтретья\nчетвертая\nпятая')
# except IOError:
#     print("Произошла ошибка ввода-вывода!")


def read_func(name='data2.txt'):
    lines_count = 0
    words_count = 0
    with open(name) as f_obj:
        for line in f_obj:
            words_count += line.split(' ').__len__()
            lines_count += 1
    return lines_count, words_count


file_name = input('Введите имя файла: ')
read_f = open(file_name, "r")
print('*' * 30, ' Выведем файл -', file_name, '*' * 30)
print(read_f.read())
read_f.close()
# вызовем функцию дающую результат
lines, words = read_func(file_name)
print('Результат подсчёта строк: ', lines, ' , слов:', words)
