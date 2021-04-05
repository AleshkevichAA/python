list_sklad = []
# хорошо бы описать константы
name_description = 'название'
price_description = 'цена'
quantity_description = 'количество'
measure_description = 'ед.'
#
print('Ввод позиции товара; просто нажмите Enter, если все данные ввели')
tovar = 'AnyData'
counter = 0
while (True):
    # инкрементируемый счетчик позиции
    counter = counter + 1
    # название
    tovar = input('Введите название: ')
    if (tovar.__len__() == 0):
        break
    # цена
    price = "AnyData"
    while (True if (not price.isdigit()) else (int(price) < 0)):
        price = input('Введите цену товара: ')
    price = int(price)
    # количество
    value = "AnyData"
    while (True if (not value.isdigit()) else (int(value) < 0)):
        value = input('Введите количество товара: ')
    value = int(value)
    # ед.
    measure = input('Введите единицы измерения: ')
    dict_pos = {name_description: tovar, price_description: price, quantity_description: value, measure_description: measure}
    tuple_data = (counter, dict_pos)
    list_sklad.append(tuple_data)
print(list_sklad)
# соберем аналитику о товарах
name_goods = []
price_goods = []
value_goods = []
measure_goods = []
for a in list_sklad:
    a = tuple(a)
    dict_tovar = dict(a[1])
    name_goods.append(dict_tovar.get(name_description))
    price_goods.append(dict_tovar.get(price_description))
    value_goods.append(dict_tovar.get(quantity_description))
    measure_goods.append(dict_tovar.get(measure_description))
dict_goods = {name_description: name_goods, price_description: price_goods, quantity_description: value_goods, measure_description: measure_goods}
print('Итоговый словарь')
print(dict_goods)
