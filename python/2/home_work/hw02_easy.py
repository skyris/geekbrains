#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from contextlib import contextmanager
from io import StringIO


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License;)"


# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: использует метод .format()
def list_of_fruits(lst):
    for i in range(len(lst)):
        print("{}. {}".format(i+1, lst[i]))


def list_of_fruits2(lst):
    for i, item in enumerate(lst):
        print("{}. {}".format(i+1, item))


# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.
def unique(lst1, lst2):
    copy_lst1 = lst1[:]
    lst1.clear()
    for item in copy_lst1:
        if item not in lst2:
            lst1.append(item)
    return lst1


# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
def list_transform(lst):
    return [item / 4 if item % 2 == 0 else item * 2 for item in lst]


# -------------------------------TEST-----------------------------------------
@contextmanager
def mock_print():
    stream = StringIO()
    original_print = __builtins__.print
    __builtins__.print = lambda x: original_print(x, file=stream)
    yield stream
    __builtins__.print = original_print
    stream.close()


class Test(unittest.TestCase):
    def test_list_of_fruits(self):
        with mock_print() as stream:
            list_of_fruits(["яблоко", "банан", "киви", "арбуз"])
            self.assertEqual(stream.getvalue(), '1. яблоко\n2. банан\n3. киви\n4. арбуз\n')

    def test_list_of_fruits2(self):
        with mock_print() as stream:
            list_of_fruits2(["яблоко", "банан", "киви", "арбуз"])
            self.assertEqual(stream.getvalue(), '1. яблоко\n2. банан\n3. киви\n4. арбуз\n')

    def test_unique_is(self):
        lst1 = [1, 2, 2, 4, 6, 8, 8, 2, 6, 0, 5]
        lst2 = [2, 8, 0]
        self.assertIs(unique(lst1, lst2), lst1)

    def test_unique(self):
        lst1 = [1, 2, 2, 4, 6, 8, 8, 2, 6, 0, 5]
        lst2 = [2, 8, 0]
        self.assertEqual(unique(lst1, lst2), [1, 4, 6, 6, 5])

    def test_list_transform_is_not(self):
        lst = [1, 2, 4, 6, 7, 8, 9, 0, 3]
        self.assertIsNot(list_transform(lst), lst)

    def test_list_transform(self):
        self.assertEqual(list_transform([]), [])
        self.assertEqual(list_transform([1, 2, 4, 6, 7, 8, 9, 0, 3]), [2, 0.5, 1.0, 1.5, 14, 2.0, 18, 0.0, 6])


if __name__ == "__main__":
    unittest.main()
