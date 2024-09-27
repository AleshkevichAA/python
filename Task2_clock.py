counter = (int)(input("Введите время в секундах:"))
# print(counter)
# вычислим часы
hour = (counter // 3600)
# вычислим минуты
minutes = (counter % 3600) // 60
# посчитаем секунды
seconds = counter % 60

print(f"Время в формате чч:мм:сс = {hour:02}:{minutes:02}:{seconds:02} ")
