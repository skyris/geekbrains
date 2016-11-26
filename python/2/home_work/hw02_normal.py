#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from contextlib import contextmanager
from io import StringIO
import math
from random import randint

__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License;)"


# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список, элементами которого будут
# квадратные корни элементов исходного списка, но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
def root_from_list(lst):
    new_list = []
    for item in lst:
        if item >= 0:
            new_item = math.sqrt(item)
            if round(new_item, 0) == new_item:
                new_list.append(new_item)
    return new_list

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
def date_to_text(date):
    date_list = date.split(".")
    month_dict = {
        1:"января", 2:"февраля", 3:"марта", 4:"апреля", 5:"мая", 6:"июня",
        7:"июля", 8:"августа", 9:"сентября", 10:"октября", 11:"ноября", 12:"декабря"
        }
    day_dict = {
        1:"первое", 2:"второе", 3:"третье", 4:"четвертое", 5:"пятое", 6:"шестое",
        7:"седьмое", 8:"восьмое", 9:"девятое", 10:"десятое", 11:"одинадцатое", 12:"двенадцатое",
        13:"тринадцатое", 14:"четырнадцатое", 15:"пятнадцатое", 16:"шестнадцатое", 17:"семнадцатое",
        18:"восемнадцатое", 19:"девятнадцатое", 20:"двадцатое", 21:"двадцать первое", 22:"двадцать второе",
        23:"двадцать третье", 24:"двадцать четвертое", 25:"двадцать пятое", 26:"двадцать шестое",
        27:"двадцать седьмое", 28:"двадцать восьмое", 29:"двадцать девятое", 30:"тридцатое", 31:"тридцать первое"
        }
    return "{} {} {} года".format(day_dict[int(date_list[0])], month_dict[int(date_list[1])], date_list[2] )


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами в диапазоне от -100 до 100
# В списке должно быть n - элементов
# Подсказка: для получения случайного числа изпользуйте функцию randint() модуля random
def fill_random(n):
    lst = []
    for i in range(n):
        lst.append(randint(-100, 100))
    return lst


# Задача-4: Дан список, заполненный произвольными целыми числами
# Получите новый список, элементами которого будут только уникальные элементы исходного
# Например, lst = [1,2,4,5,6,2,5,2], нужно получить lst2 = [1,4,6]
def unique_list(lst):
    return list(set(lst))


class Test(unittest.TestCase):
    def test_root_from_list(self):
        self.assertEqual(root_from_list([2, -5, 8, 9, -25, 25, 4]), [3, 5, 2])

    def test_date_to_text(self):
        self.assertEqual(date_to_text("02.11.2013"), "второе ноября 2013 года")

    def test_fill_random(self):
        pass

if __name__ == "__main__":
    unittest.main()