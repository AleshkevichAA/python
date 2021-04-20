my_list = [7, 5, 3, 3, 2]
# Обеспечим ввод искомого значения
new_number = '0'
print(
    '   -----========= Рейтинг ===========-------------\nПри вводе данных, отличающихся от натуральных чисел программа прекращает свою работу.')
print(my_list)
while (True if (new_number.isdigit()) else int(new_number) >= 0):
    new_number = input('Введите натуральное число: ')
    if (new_number.isdigit()):
        my_list.append(int(new_number))
        my_list.sort()
        my_list.reverse()
        print(my_list)
