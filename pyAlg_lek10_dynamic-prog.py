"""
Бинарный поиск. Динамическое проектирование.
Алгоритмы на Python 3. Лекция №10
https://youtu.be/EdhN_gEDfUM Тимофей Хирьянов
05/11/2020
"""
###

"""
Реализация бинарного поиска.
Массив должен быть отсортирован!
"""

def left_bound(A, key):
    """Поиск левой границы в массиве А
    по ключю key
    """
    left = -1
    right = len(A)
    while right - left > 1: #пока границы не сомкнутся
        middle = (left + right) // 2 # "стреляем" в середину диапазона
        if A[middle] < key:
            left = middle
        else:
            right = middle

    return left

def right_bound(A, key):
    """Поиск правой границы в массиве А
    по ключю key
    """
    left = -1
    right = len(A)
    while right - left > 1: #пока границы не сомкнутся
        middle = (left + right) // 2 # "стреляем" в середину диапазона
        if A[middle] <= key:
            left = middle
        else:
            right = middle

    return right



M = [1, 3, 3, 6, 7, 7, 9]

R = right_bound(M, 9)



""" Динамическое проектирование
Числа Фибоначчи: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
Функция вычисления ЧФ методом рекурсии (очень плохая асимптотика!)"""

def fib_r(n):
    """Вычисление числа Фибоноаччи рекурсивным способом"""
    if n <= 1:
        return n #крайний случай
    return (fib_r(n-1) + fib_r(n-2))



def fib(n):
    """Вычисление числа Фибоноаччи динамическим способом"""
    fib = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]



"""Исполнитель - кузнечик.
Сколько способов кузнечику попасть в точку N прыжками +1 и +2?
Дополнительно: шаг +3, запрещённые точки"""





def count_min_cost(N, price:list):
    """ Функция рассчета минимальной стоимости посещения клетки N"""
    K = [0, 1] + [0]*(N-1) #количество траекторий
    C = [float("-inf"), price[1], price[1] + price[2]] + [0]*(N-2) #стоимость
    for i in range(3, N+1):
        K[i] = K[i-1] + K[i-2] + K[i-3]
        C[i] = price[i] + min(C[i-1], C[i-2])
    print("число N:", N, "кол. траекторий:", K[N], " мин. стоимость:", C[N])


N= 5
PriceList = [i for i in range(N+1)]

count_min_cost(N, PriceList)



    
    


