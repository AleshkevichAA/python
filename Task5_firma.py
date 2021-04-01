debet = (int)(input("Введите доход фирмы "))
credit = (int)(input("Введите расходы фирмы "))

if (debet>credit):
    print("Прибыль = ",(debet-credit))
    print("Рентабельность = %.4f"%((float)(debet/credit)))
    persons=(int)(input("Введите численность сотрудников "))
    print("Поздравляю, Вы блестящий руководитель, прибыль на одного сотрудника составляет = %.2f"%(float)((debet-credit)/persons))
elif (debet<credit):
    print("Убыток = ", (credit-debet))
else:
    print("Прибыль равна убытку, идеально для налоговой отчетности")

