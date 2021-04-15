# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file_in='data4_in.txt'
file_out='data4_out.txt'


with open(file_in, 'r', encoding='UTF-8') as f_obj:
    while True:
        line = f_obj.readline()
        if line == '':
            break
        # добавим строку во второй файл
        with open(file_out, 'a', encoding='UTF-8') as f_wr:
            data_line=line.split(' — ')
            f_wr.write(my_dict.get(data_line[0])+' — '+data_line[1])

with open(file_out, 'r', encoding='UTF-8') as f_read:
    print(f_read.read())
