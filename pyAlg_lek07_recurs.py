"""
Рекурсия.
Алгоритмы на Python 3. Лекция №7
https://www.youtube.com/watch?v=0Bc8zLURY-c Тимофей Хирьянов
23/10/2020
"""

from modules import graphics as gr

window = gr.GraphWin("Рекурсия", 600, 600)


def matryoshka(n):
    if n == 1:
        print("Матрёшечка")
    else:
        print("Верх матрёшки n=", n)
        matryoshka(n-1)
        print("Низ матрешки n=", n)

alpha = 0.1 #глобальная переменная для разбиения отрезка

def fractal_rectangle(A, B, C, D, deep=10):
    """
    Рисование вложенных прямоугольников методом рекурсии.
    A, B, C, D - координаты (x, y).
    deep - максимальная глубина рекурсии

    """
    if deep < 1: #глубина функции достигла максимума
        return #выход из рекурсии

    # Цикл перебора точек квадрата (по двум переменным - пары точек), *A - разворачивание списка, кортежа
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0]*(1-alpha)+ B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
    B1 = (B[0]*(1-alpha)+ C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
    C1 = (C[0]*(1-alpha)+ D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
    D1 = (D[0]*(1-alpha)+ A[0]*alpha, D[1]*(1-alpha) + A[1]*alpha)

    fractal_rectangle(A1, B1, C1, D1, deep-1) #вызов рекурсивной фун
    
    
fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), 100)


def factorial(n: int):
    assert n >= 0, "Факториал числа не определен!"
    if n == 0: #крайний случай
        return 1
    return factorial(n-1)*n


def gcd(a, b):
    """ Алоритм Евклида - НОД
    Greatest common divisor - GCD
    """
    if a == b:
        return a #крайний случай
    elif a > b:
        return gcd(a - b, b)
    else: #a < b
        return gcd(a, b - a)


def gcd_(a, b):
    """ Алоритм Евклида - НОД (b, a%b)
    Greatest common divisor - GCD
    усовершенств.
    """
    if b == 0:
        return a
    else:
        return gcd_(b, a%b)

def gcd_fun(a, b):
    """ Алоритм Евклида - НОД (b, a%b)
    Greatest common divisor - GCD
    усовершенств., в функциональном стиле
    """
    return a if b == 0 else gcd_fun(b, a%b)


def pow(a: float, n: int):
    """ Быстрое возведение в степень
    a^n = a^(n-1)*a, n >0 - рекурсия!
    """
    if n == 0:
        return 1
    elif n%2 == 1: # n - НЕЧЁТ
        return pow(a, n-1)*a
    else: # n - ЧЁТНОЕ
        return pow(a**2, n//2) # a^n = (a^2)^(n/2) - быстрое понижение степени!
    
