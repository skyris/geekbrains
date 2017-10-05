#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from contextlib import contextmanager
from contextlib import redirect_stdout
from io import StringIO

__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License;)"


# Задача-1: Дано произвольное целое число, вывести поочередно цифры исходного числа
def arbitrary_number(num):
    lst = []
    for digit in str(num):
        lst.append(int(digit))
    return lst

# VictorKlimov: Читая "на вход дано число" у меня всегда возникает вопрос, а нужно ли это проверять?
# VictorKlimov: Когда имеет смысл проверять вход?
# VictorKlimov: И как лучше проверять? ассертом, ифом?


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так: print("a = ", b, "b = ", a) - это неправильное решение!
def swap():
    a = input("Введите a: ")
    b = input("Введите b: ")
    a, b = b, a  # Можно через tmp, но зачем?
    return "a={0}, b={1}".format(a, b)


# Задача-3: Запросите у пользователя его возраст. Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
def age_verification():
    while True:
        try:
            age = int(input("Введите Ваш возраст: "))
            break
        except ValueError:
            print("Введите возраст цифрами.")
    if age < 18:
        print("Извините, пользование данным ресурсом только с 18 лет")
    else:
        print("Доступ разрешен")


# Дальше тестируем:)
# В процессе тестирования разобрался:
# 1) как использовать unittest. Возможно не совсем правильно.
# 2) Как подменять input
# 3) Подменять print
# и попутно наконец понял как работает контекстный менеджер
class TestFirstTask(unittest.TestCase):

    def test_first_task(self):
        self.assertEqual(arbitrary_number(578), [5, 7, 8])
        self.assertEqual(arbitrary_number(8905), [8, 9, 0, 5])
        self.assertEqual(arbitrary_number(359487), [3, 5, 9, 4, 8, 7])



@contextmanager
def mock_input(value):
    """
    Контекстный менеджер "подделывающий" функцию input
    :param value: генератор ответов
    :return:
    """
    original_input = __builtins__.input
    __builtins__.input = lambda _: next(value)  # итерация по генератору
    yield
    __builtins__.input = original_input


def helper_for_gen(*args):
    """
    Решает задачу, когда нужно "подделать" несколько функций input
    :param args: ответы пользователя
    :return: генератор
    """
    for arg in args:
        yield arg


ski = True


# @unittest.skipIf(ski == True, "fuck you  ")
class TestWithMockingInputAndPrint(unittest.TestCase):

    def setUp(self):
        self.stream = StringIO()
        self.write_to_stream = redirect_stdout(self.stream)

    def tearDown(self):
        self.stream.close()

    def test_second_task_1(self):
        gen = helper_for_gen(80, 90)
        with mock_input(gen):
            res = swap()
        self.assertEqual(res, "a={0}, b={1}".format(90, 80))

    def test_second_task_2(self):
        gen = helper_for_gen(1, 2)
        with mock_input(gen):
            res = swap()
        self.assertEqual(res, "a={0}, b={1}".format(2, 1))
    @unittest.expectedFailure
    def test_second_task_3(self):
        gen = helper_for_gen(10, 10)
        with mock_input(gen):
            res = swap()
        self.assertEqual(res, "a={0}, b={1}".format(11, 10))

    def test_third_task_young(self):
        gen = helper_for_gen("17")
        with mock_input(gen), self.write_to_stream:
            age_verification()
        self.assertEqual(self.stream.getvalue(), 'Извините, пользование данным ресурсом только с 18 лет\n')

    def test_third_task_18(self):
        gen = helper_for_gen("18")
        with mock_input(gen), self.write_to_stream:
            age_verification()
        self.assertEqual(self.stream.getvalue(), 'Доступ разрешен\n')

    def test_third_task_old(self):
        gen = helper_for_gen("59")
        with mock_input(gen), self.write_to_stream:
            age_verification()
        self.assertEqual(self.stream.getvalue(), 'Доступ разрешен\n')


if __name__ == '__main__':
    unittest.main()
