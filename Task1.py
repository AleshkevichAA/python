def divide(a=float(input('Введите делитель: ')), b=float(input('Введите делимое: '))):
    if (b == 0):
        return 'Деление на 0 недопустимая операция'
    return a / b
print(divide())
