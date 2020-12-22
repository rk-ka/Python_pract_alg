
""" Динамическое программирование.
Алгоритмы на Python 3. Лекция №11

https://youtu.be/m4HOkVeN4Mo Тимофей Хирьянов
20/11/2020 """


def lcs(A:list, B:list):
    """Задача нахождения наибольшей общей 
    длины подпоследовательности - 
    Longest common subsequence, LCS."""

    F = [[0]*(len(B) + 1) for i in range(len(A) + 1)] #выделение памяти, зануление массива
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[-1][-1] #последний эл-т в последней строке


def lcs_p(A:list, B:list):
    """Задача нахождения наибольшей общей 
    длины подпоследовательности - 
    Longest common subsequence, LCS."""

    F = [[0]*(len(B) + 1) for i in range(len(A) + 1)] #выделение памяти, зануление массива
    
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            print(A[i-1], B[j-1])
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
                
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
            print(F, "\n")
    return F[-1][-1] #последний эл-т в последней строке


# НЕ ДОСТОРЕРНО
def gis(A:list):
    """ Наибольшая возрастающая подпоследовательность (НВП)"""
    F = [0]*(len(A) + 1)
    for i in range(1, len(A) + 1):
        
        m = 0 # максимум, крайний случай
        for j in range(0, i):
            if A[i-1] > A[j-1] and F[j] > m:
                m = F[j]
        F[i] = m + 1
        print(F)
    return F[len(A)]


# ИЗ ФОРУМА
def gis2(A:list):
    """Длина наибольшей возрастающей подпоследовательность массива."""
    F = [0]*len(A)
    for i in range(len(A)):
        m = 0
        for j in range(i):
            if A[i] > A[j] and F[j] > m:
                m = F[j]
        F[i] = m + 1
        print(F)
    return max(F) if F else 0


            






A = [1, 1, 2, 2, 3, 3]
A1 = [2, 2, 3, 3, 4, 4]
A2 = [1, 2, 3, 4, 5]
A3 = [3, 4, 5, 6, 7]

B = [1, 2, 3, 4]
B1 = [3, 4, 5, 6]

D = [2, 5, 6, 7, 0, 2, 9]

print("Длина общей подпоследовательности", B, B1, "\n", lcs(B, B1))
print("Наибольшая возрастающая последоватьельность, длина", D, gis(D)) 

print("НВП вариант 2", D, gis2(D))

