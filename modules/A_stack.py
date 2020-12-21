# -*- coding: cp1251 -*-


""" 
������ �13. ��������� �� Python 3.
��������� ������

https://youtu.be/L4IU1bPKvHM ������� ��������
02/12/2020


# # #
����� ������

C�������� ������ ����/stack ��� ������� LIFO
Use case (������ �������������):

(������������� doctest)


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

_stack = [] # ���������� ����������


#������-������ ���������� ������� ������
#���������� ����� ��������, ���������� �� ����������

def push(x):
    """
    ��������� ������� x � ����� �����
    (������������ doctest)

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
    #���������� ������� ������������ �� ����������-������
    import doctest
    doctest.testmod() #������ ���� ��
    #doctest.testmod(verbose=True) #� �����������




    






    
