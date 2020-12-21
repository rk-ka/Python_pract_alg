"""
МОДУЛЬ ДЛЯ
Лекция №13. Алгоритмы на Python 3.
Структуры данных.

https://youtu.be/L4IU1bPKvHM Тимофей Хирьянов
02/12/2020

"""

from modules import A_stack


def is_braces_seq_correct(s: str):
    """
    Проверяет корректность скобочной последовательности
    из круглых и квадратных скобок () []

    >>> is_braces_seq_correct("(([()]))[]")
    True
    >>> is_braces_seq_correct("([)]")
    False
    >>> is_braces_seq_correct("([]")
    False
    >>> is_braces_seq_correct("]")
    False
    >>> is_braces_seq_correct("(")
    False
    """
    for brace in s:
        if brace not in "()[]": #встроенный поиск строки в подстроке (хуже чем КМП)
            continue #пропуск итерации
        if brace in "([":
            A_stack.push(brace)
        else:
            #Я утверждаю что: ..., иначе:
            assert brace in ")]", "Ожидалась закрывающая скобка:" + str(brace)
            if A_stack.is_empty():
                return False
            left = A_stack.pop()
            assert left in "([", "Ожидалась закрывающая скобка:" + str(brace)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != brace:
                return False
                
    return A_stack.is_empty()
    



if __name__ == "__main__":
    #встроенная функция тестирования из документов-строки
    import doctest
    doctest.testmod() #молчит если ОК
    #doctest.testmod(verbose=True) #с оповещением
