#Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    inp_data_a = float(input("Введите делимое: "))
    inp_data_b = float(input("Введите делитель: "))
    if (inp_data_b == 0):
        raise MyException("Ошибка! Вы ввели делимое число - 0. Результата не будет.")
except ValueError:
    print("Вы ввели не число")
except MyException as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {inp_data_a/inp_data_b}")