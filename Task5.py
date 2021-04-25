# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        self.a += other.a
        self.b += other.b
        return self

    def __mul__(self, other):
        self.a = self.a * other.a - self.b * other.b
        self.b = self.a * other.b + self.b * other.a
        return self

    def out(self):
        print(str(self.a) + ('+' if (self.b > 0) else '') + str(self.b) + 'i')


first = ComplexNumber(2, 3)
second = ComplexNumber(4, 5)
first = first + second
first.out()
first = ComplexNumber(2, 3)
first = (first * second)
first.out()
