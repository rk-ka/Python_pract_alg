#Функция описательная с параметрами

def Hello(name = "World"):
    print("Hello, ", name)


# Функция с return (чистая функция)

def max2(x,y):
    if x > y:
        return x

    return y

def max3(x,y,z):
    return max2(x, max2(y,z))


def hello_separated(name="World", separator = "-"):
    print("Hello,", name, sep=separator)


def build_house(window, up_left_corn, size):
    """Функция рисует дом"""
    height = design(size)
    pass



""" Метод грубой силы - Bruteforce (перебор значений)"""

def is_simple_number(x):
    """ Определяет, является ли число простым.
    x - целое, положительное
    Если простое, то возвращает True
    """
    divisor = 2 #ДЕЛИТЕЛЬ       
    while divisor < x:
        if x%divisor == 0: # Если число делится на делитель
            return False
        divisor += 1
    return True


def factorize_number(x):
    """Раскладывает число на множетели.
    Печатаем на экран.
    х - целое положительное
    """
    divisor = 2
    while x > 1:
        if x%divisor == 0:
            print(divisor)
            x //= divisor # x = x/divisor
        else:
            divisor += 1
            
        
        
        
