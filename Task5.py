# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

file_in = 'data5.txt'
from random import randint


def generate_num(counter=10):
    res = ''
    i = 0
    while (i < counter):
        i += 1
        res = res + str(randint(1, 100)) + ' '
    #обрежем последний символ
    return res[:(res.__len__()-1)]


with open(file_in, 'w', encoding='UTF-8') as f_obj:
    f_obj.write(generate_num(10))
with open(file_in, 'r', encoding='UTF-8') as f_obj:
    data_list = f_obj.read().split(' ')
    print(data_list)
    sum = 0
    for i in data_list:
        sum+=int(i)
    print('Сумма чисел: ',sum)