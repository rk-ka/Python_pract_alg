# -*- coding: cp1251 -*-


""" 
Лекция №13. Алгоритмы на Python 3.
Структуры данных

https://youtu.be/L4IU1bPKvHM Тимофей Хирьянов
02/12/2020


# # #
ПИШЕМ МОДУЛЬ

Cтруктура данных стек/stack или очередь LIFO
Use case (пример использования):

(Текстирование doctest)


>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True

"""

_stack = [] # глобальная переменная


#Модуль-обёртка стандарных методов списка
#реализайия может меняться, независимо от интерфейса

def push(x):
    """
    Добавляет элемент x в конец стека
    (тестирование doctest)

    >>> size = len(_stack)
    >>> push(5)
    >>> len(_stack) - size
    1
    >>> _stack[-1]
    5
    """
    _stack.append(x)

def pop():
    x = _stack.pop()
    return x

def clear():
    _stack.clear()

def is_empty():
    return len(_stack) == 0


if __name__ == "__main__":
    #встроенная функция тестирования из документов-строки
    import doctest
    doctest.testmod() #молчит если ОК
    #doctest.testmod(verbose=True) #с оповещением




    






    
