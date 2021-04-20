# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(var1,var2,var3):
    arg_list=[float(var1),float(var2),float(var3)]
    print(arg_list)
    arg_list.sort(reverse=True)
    print(arg_list)
    return arg_list[0]+arg_list[1]
print(my_func(input('Введите первое число: '),input('Введите второе число: '),input('Введите третье число: ')))