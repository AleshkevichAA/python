# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

list_20_21 = [first_el for first_el in range(20, 241) if (first_el % 20 == 0 or first_el % 21 == 0)]
print(list_20_21)
