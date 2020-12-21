# -*- coding: cp1251 -*-


""" Редакционное расстояние Левинштейна -
динамическое программирование (продолжение) 

Алгоритмы на Python 3. Лекция №12

https://youtu.be/rEPggzaPoUw Тимофей Хирьянов
26/11/2020 """


def levenstein (A:list, B:list):
    """Редакционное растояние между двумя последовательностями (словами)
    F - ред. расстояние, индексы i, j c учетом 0: (len(L) + 1)
    O(m*n)
    """

    #заполняем 2мерн. массив и вычисляем крайний случай
    # заполням матрицу 
    F =[[(i + j) if i*j == 0 else 0 for j in range(len(B) + 1)]
        for i in range(len(A) + 1)]
    
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            #если эл-ты равны, то расстояние не увеличивается
            if A[i-1] == B [j-1]: #начиная с первого эл-та в строках
                F[i][j] = F [i-1][j-1]
            else:
                F[i][j] = 1 + min(F[i-1][j], F[i][j-1], F[i-1][j-1])

    return F[len(A)][len(B)]
                

def equal (A, B):
    """ Проверка равенства строк (наивный алгоритм) O(n)"""
    if len(A) != len(B): #если длина строк не равна - выходим
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True

    
    



A = [0, 0, 0]
B = [0, 1, 2, 3]

R = levenstein(A, B)
print(A, B, "\n levenstein:", R)

