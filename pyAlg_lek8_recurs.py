"""
Рекурсия - Hard way!
Алгоритмы на Python 3. Лекция №8
https://www.youtube.com/watch?v=2XFaK3bgT7w Тимофей Хирьянов
27/10/2020
"""
import time
t = 1 #delay
#time.sleep(t)

# Генерация всех перестановок

def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
    else:
        gen_bin(M-1, prefix+"0")
        gen_bin(M-1, prefix+"1")
        
    
print_flag = False #вывод принтов




def gen_numbers(N: int, M: int, prefix=None):
    """
    Генерирует все числа (с лидирующими нулями)
    в N-ричной системе счисления (N <= 10)
    Упрощенная задача генерации последовательности
    N цифр: {0,...,N-1}, начиная с prefix, M кол. чисел
    """
    prefix = prefix or [] # <=> if prefix == None: prefix = [] - пустой список
    if M == 0: # крайний случай
        print(prefix)
        return
    
    for digit in range(N):
        prefix.append(digit)
        if print_flag: print("digit", digit) 
        if print_flag: print("gen_number(", N, M-1, prefix, ")") 
        gen_numbers(N, M-1, prefix) #рекурентный вызов в цикле
        prefix.pop() #удаление последней цифры - лист



def find(number, A):
    """ищет х в А и возвращает True, если такой есть.
    False - если такого нет.
    """
    for x in A:
        if number == x:
            return True
    return False

def gen_permutations(N:int, M:int=-1, prefix=None):
    """ Генерация перестановок N чисел в М позициях,
    с prefix
    """
    M = N if M == -1 else M # по умолчанию N чисел в N позициях
    prefix = prefix or []

    if M==0:
        print(*prefix) #развернуть список
        return
    for number in range(1, N+1):
        if print_flag: print("number =", number)
        if find(number, prefix): # необходимо исключить бывшие в исп. числа
            if print_flag: print("skip:", number) ##
            continue #пропускаем итерацию цикла, минуя тело цикла
        prefix.append(number)
        if print_flag: print("> gen_permutations(",N, M-1, prefix, ")") ##
        gen_permutations(N, M-1, prefix)
        prefix.pop()


gen_permutations(3)
   
