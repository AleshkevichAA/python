num = (int)(input("Введите положительное число "))
if (num < 0):
    print("Это число меньше 0 : ", num)
    exit(83)
max = 0
while (num / 10 > 0):
    if (num % 10 > max):
        max = num % 10
        # если 9, дальше искать смысла нет, больше не будет
        if (max == 9):
            break
    num = (int)(num / 10)
print("Максимальная цифра", max)
