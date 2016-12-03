#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License;)"


# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
lst = [1, 2, 4, 0]


def gen(lst):
    return (x**2 for x in lst)


def function_generator(lst):
    for x in lst:
        yield x**2


map_object = map(lambda x: x**2, lst)


# Задание-2:
# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.


def both(lst, lst2):
    return (x for x in lst if x in lst2)


def both2(lst, lst2):
    for x in lst:
        if x in lst2:
            yield x


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих след. условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


def weird_list(lst):
    for x in lst:
        if x >= 0 and x % 3 == 0 and x % 4 != 0:
            yield x


def weird_list2(lst):
    return (x for x in lst if x >= 0 and x % 3 == 0 and x % 4 != 0)


# ------------------------------TEST--------------------------------------------


class Test(unittest.TestCase):
    def test_gen(self):
        res = gen([5, 3, 9, 8])
        for i in range(len([5, 3, 9, 8])):
            next(res)

        new_lst = []
        for x in gen([]):
            new_lst.append(x)
        self.assertEqual(new_lst, [])

        new_lst = []
        for x in gen([1, 2, 4, 0]):
            new_lst.append(x)
        self.assertEqual(new_lst, [1, 4, 16, 0])

    def test_function_generator(self):
        res = function_generator([5, 3, 9, 8])
        for i in range(len([5, 3, 9, 8])):
            next(res)

        new_lst = []
        for x in function_generator([]):
            new_lst.append(x)
        self.assertEqual(new_lst, [])

        new_lst = []
        for x in function_generator([1, 2, 4, 0]):
            new_lst.append(x)
        self.assertEqual(new_lst, [1, 4, 16, 0])

    def test_map_object(self):
        res = map(lambda x: x**2, [5, 3, 9, 8])
        for i in range(len([5, 3, 9, 8])):
            next(res)

        new_lst = []
        for x in map(lambda x: x**2, []):
            new_lst.append(x)
        self.assertEqual(new_lst, [])

        new_lst = []
        for x in map(lambda x: x**2, [1, 2, 4, 0]):
            new_lst.append(x)
        self.assertEqual(new_lst, [1, 4, 16, 0])

    def test_both(self):
        new_lst = []
        for x in both([1, 2, 3, 4, 5], [2, 4, 6, 8]):
            new_lst.append(x)
        self.assertEqual(new_lst, [2, 4])

    def test_both2(self):
        new_lst = []
        for x in both2([1, 2, 3, 4, 5], [2, 4, 6, 8]):
            new_lst.append(x)
        self.assertEqual(new_lst, [2, 4])

    def test_weird_list(self):
        new_lst = []
        for x in weird_list(list(range(-30, 30))):
            new_lst.append(x)
        self.assertEqual(new_lst, [3, 6, 9, 15, 18, 21, 27])

    def test_weird_list2(self):
        new_lst = []
        for x in weird_list2(list(range(-30, 30))):
            new_lst.append(x)
        self.assertEqual(new_lst, [3, 6, 9, 15, 18, 21, 27])


if __name__ == "__main__":
    unittest.main()
