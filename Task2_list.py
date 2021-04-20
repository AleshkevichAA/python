print('Введите данные элементов списка, нажимая Enter. Для окончания ввода просто Enter.')
int
counter = 0
list_data = []
checker = True
while (checker):
    counter = counter + 1
    element = input('Элемент %i' % counter + ':')
    if (element == ''):
        checker = False
    else:
        # добавим элемент
        list_data.append(element)
print('Выведем список после ввода данных ', list_data)
# поменяем четные с нечетными местами
list_data2 = []
counter = 0
while (counter < list_data.__len__()):
    element = list_data[counter]
    if (counter % 2 == 1):
        list_data2.insert(counter-1,element)
    else:
        list_data2.append(element)
    counter = counter + 1
print(list_data2)
