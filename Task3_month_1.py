# Вариант с листом
list_months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
               'Декабрь']
list_seasons = ['Зима', 'Весна', 'Лето', 'Осень']
# Обеспечим ввод искомого значения
month = '0'
while (True if (not month.isdigit()) else ((int(month) < 1) | (int(month) > 12))):
    month = input('Введите номер месяца (1-12) ')
month = int(month)
print('Месяц - ', list_months[month - 1], end=', время года - ')
print(list_seasons[0]) if ((month in range(0, 3)) | (month == 12)) else (
    print(list_seasons[1]) if (month in range(3, 6)) else (
        print(list_seasons[2]) if (month in range(6, 9)) else print(list_seasons[3])))

# Решение со словарём
print('-==- ' * 40)
print('Словарь(часть 2)')
dict_calendar = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
month = '0'
while (True if (not month.isdigit()) else ((int(month) < 1) | (int(month) > 12))):
    month = input('Введите номер месяца (1-12) ')
month = int(month)
for key_seasons in dict_calendar.keys():
    list_number_months = list(dict_calendar.get(key_seasons))
    for temp_month in list_number_months:
        if (temp_month == month):
            print('Сезон года - ', key_seasons)
