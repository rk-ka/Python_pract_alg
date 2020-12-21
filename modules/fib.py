
def fib(n):
    """Вычисление числа Фибоноаччи динамическим способом
    
    для  unittest (practPy_lek14_TDD.py)
    Вычисляет число Фибоначчи от n.
    Выбрасывает исключение
    TypeError, не целое число,
    ValueError, если число отрицательное или больше допустимого (по контракту).
    
    :param n: целое число от 0 до 9999
    :return: целое число от 0 до ..(?)
    
    """
    
    if not isinstance(n, int):
        raise TypeError("Fibonacci function only work with int type")

    if n < 0:
        raise ValueError("Fibonacci can't work with negative numbers")

    if n >= 10000:
        raise ValueError("Fibonacci can't work with numbers large than 9999")

    if n == 0:
        return 0
    
    f_2 = 0
    f_1 = 1
    for i in range(2, n + 1):
        f_1, f_2 = (f_1 + f_2), f_1
    return f_1

        

    
    """ старая реализация
    fib = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
    """

