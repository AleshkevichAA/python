# 1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31 22
# 37 43
# 51 86
# 3 5 32
# 2 4 6
# -1 64 -8
# 3 5 8 3
# 8 3 7 1
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    my_list = []

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        res = '\n'
        for i in self.my_list:
            res += f'{i}\n'
        return res

    def __add__(self, other):
        result = []
        for i in range(len(self.my_list)):
            list_str = []
            for j in range(len(self.my_list[0])):
                list_str.append(int(self.my_list[i][j]) + int(other.my_list[i][j]))
            result.append(list_str)
        self.my_list = result
        return self


data1 = []
matrix = Matrix([[31, 32], [37, 43], [51, 86]])
matrix2 = Matrix([[131, 132], [137, 143], [151, 186]])
print('Матрица 1:', matrix)
print('Матрица 2:', matrix2)
matrix3 = matrix + matrix2
print('Итоговая матрица:', matrix3)
