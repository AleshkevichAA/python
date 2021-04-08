# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    """
    :param word: слово
    :return: слово с заглавной буквы
    """
    return str(word).capitalize()


def parse_func(param):
    """
    :param param: строка слов
    :return: строка с заглавными буквами во всех словах
    """
    list_result = []
    for small_word in list(param.split()):
        list_result.append(int_func(small_word))
    return " ".join(list_result)


result = parse_func(input('Введите строку слов: '))

print(result)
