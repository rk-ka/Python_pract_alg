"""
Алгоритмы на Python 3. Лекция №6
Способы сортировки массива
https://www.youtube.com/watch?v=NLq7nB9bV0M&t=2671s Тимофей Хирьянов
21/10/2020
"""

# 1. В начале создадим mock-up функции с pass.
# 2. Создадим тестирующие функции, добъемся их выполнения c с результатом "Fail".
# 3. Напишем функции. -> тестирование ОК


def insert_sort(A):
    """ сортировка списка А вставками """
    N = len(A) #длина списка 
    for top in range(1, N): #расширение области массива  
        k = top # k - временное положение изменяемого элемента
        #пока к - не стоит в первой позиции слева и предидущ. эл-т > посдед.
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k] # сдвиг с обменом
            k -= 1
    
    

def choise_sort(A):
    """ сортировка списка А выбором """
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            # pos - позиция в массиве, k- позиция кандидата на место pos
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

    


def bubble_sort(A):
    """ сортировка списка А методом пузырька"""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
                            



# Реализуем тестирование с помощью функций

def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__) #исп. документ-строку исп. фун.

    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A) #run fun
    # поэлементное сравнение списков - затратная операция
    print("OK" if A == A_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list (range(0, 10)) #сложение списков
    A_sorted = list(range(20))
    sort_algorithm(A) #run fun
    # поэлементное сравнение списков - затратная операция!
    print("OK" if A == A_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A) #run fun
    # поэлементное сравнение списков - затратная операция!
    print("OK" if A == A_sorted else "Fail")

if __name__ == "__main__":
    #запускаем фун тестирования, передаем ей фун сортировки
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)

    

