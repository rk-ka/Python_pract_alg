""" 
Лекция №14. Практика на Python 3.
Опережающее тестирование - TDD

https://youtu.be/Th2D6B1kPOc Тимофей Хирьянов
04/12/2020
"""



import unittest


"""
# https://docs.python.org/3/library/unittest.html
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

"""

from modules.fib import fib
##def fib(n):
##    """
##    Вычисляет число Фибоначчи от n.
##    Выбрасывает исключение
##    TypeError, не целое число,
##    ValueError, если число отрицательное или больше допустимого (по контракту).
##    
##    :param n: целое число от 0 до 9999
##    :return: целое число от 0 до ..(?)
##
##    """
##
##    pass
 


class TestFibonacci(unittest.TestCase):

    def test_simple(self):
        #проверка на корректность значений тестируемуй функции
        for param, result in [(0, 0), (1, 1), (2, 1), (3, 2), (10, 55)]:
            self.assertEqual(fib(param), result) #проверка равенства


    def test_stress(self):
        self.assertEqual(fib(9999), fib(9998) + fib(9997))
        # with - менеджер контекста, стозд спец. ситуацию для поломки фун.
        with self.assertRaises(ValueError):
            fib(10000)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fib(-1)
        with self.assertRaises(ValueError):
            fib(-100)            

    def test_wrong_param_type(self):
        with self.assertRaises(TypeError):
            fib(2.5)
        with self.assertRaises(TypeError):
            fib('Hello')            
            





if __name__ == '__main__':
    unittest.main()
