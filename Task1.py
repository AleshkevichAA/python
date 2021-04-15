# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.
try:
    with open("text.txt") as f_obj:
        f_obj.write('')
except IOError:
    print("Произошла ошибка ввода-вывода!")

out_f = open("out_1.txt", "w")
while True:
    data =input('Введите строку, пустая строка конец ввода:')
    if (data==''):
        out_f.close()
        break
    out_f.write(data+'\n')
out_f.close()

read_f = open("out_1.txt", "r")
print(read_f.read())
read_f.close()

