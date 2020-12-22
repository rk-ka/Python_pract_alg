"""
Рекурсивные сортировки.
Алгоритмы на Python 3. Лекция №9
https://www.youtube.com/watch?v=qf82-r9hl2Y Тимофей Хирьянов
29/10/2020
"""

A = [2, 4, 6]
B = [1, 3, 4, 5]

print_flag = False


""" Сортировка слиянием / MergeSort """

def merge(A: list, B: list):
    """Объединение списков A и B"""
    C = [0]*(len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1

    while i < len(A): #доливаем остаток списка А
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B): #доливаем остаток списка В
        C[n] = B[k]
        k += 1
        n += 1

    return C


def merge_sort(A):
    """Сортировка слиянием рекурсивная"""
    if len(A) <= 1: #крайний случай
        return # сортируем данный нам массив, не возвращаем!
        #return A - вовращ. отсортиров массив 
    
    middle = len(A)//2
    L = [A[i] for i in range(0,middle)] #левая часть списка, без исп. срезов
    R = [A[i] for i in range(middle, len(A))] #правая часть списка

    if print_flag: print("L:", L)
    if print_flag: print("R:", R)
    
    merge_sort(L) #рекурентный вызов
    merge_sort(R)
    
    C = merge(L, R) #объединяем массивы

    if print_flag: print("merge:", L, R, "C=", C)
     
    #! А = C не подходит!, т.к. ссылается на внутр. переменные фун.
    for i in range(len(A)): #присваиваем, без срезов
       A[i] = C[i]
       
       
    
    
M = [7,4,6,7,4,2,7,9,5,2,6,9,4,8,1]
# 1 2 2 4 4 4 5 6 6 7 7 7 8 9 9

##M0 = [4, 2, 6, 3, 1, 4, 5]
##print("sort: ", M)
##merge_sort(M)
##print(*M)


""" Сортировка Тони Хоара / QuickSort """

def hoar_sort(A):
    """ Сортировка Тони Хоара / QuickSort """
    if len(A) <= 1: #! крайний случай
        return #None
    barrier = A[0] #принимаем барьерный эл-т равный первому
    L = []; M = []; R =[] #проще, но исп. доп. память
    #! L = M = R = [] нельзя, т.к. ссылка на один объект []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)

    hoar_sort(L) #рекур. вызов
    hoar_sort(R)

    k = 0
    for x in L + M + R: #исп. доп. память для краткости
        A[k] = x
        k += 1
        
    


hoar_sort(M)
print(*M)


""" Проверка сортировки массива """

def check_sorted(A, ascending=True):
    """ Проверка отсортированности массива
    за O(len(A)) - однопроходный.
    По умолчанию - по возрастанию.
    """
    flag = True

    # Проверка на возростание
    # int(True) = 1; int(False) = 0
    # ascending(True) -> +1 ; ascending(False) -> -1
    s = 2 * int(ascending) - 1

    N = len(A)
    for i in range(0, N-1):
        if s * A[i] > s * A [i+1]:
            flag = False
            break
    return flag
    

    
   


    
