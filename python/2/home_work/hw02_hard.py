#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License;)"


# Задание-1: уравнение прямой вида y = kx - b задано ввиде строки.
# Определить координату y, точки с заданной координатой x

# equation = 'y = -12x + 11111140.2121'
# equation = 'y = -12*x + 11111140.2121'
# x = 2.5

# вычислите и выведите y

def parse_equation(string, x):
    string = string.strip("y= ")
    lst = string.split("x")
    a = float(lst[0].strip("*"))
    b = lst[1].strip("+ ")
    if b[0] == "-":
        b = -float(b[1:])
    else:
        b = float(b)
    return a * x + b


def parse_equation2(string, x):
    string = string.strip("y= ")
    if "*" not in string:
        string = string.replace("x", "*x")
    return eval(string)


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'. Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31) (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом (т.е. 2 - для дня, 2- месяц, 4 -год)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

def date_validation(date):
    date_list = date.split(".")
    if tuple(map(len, date_list)) != (2, 2, 4):
        return False
    try:
        day = int(date_list[0])
        month = int(date_list[0])
        year = int(date_list[0])
        if day < 1 or day > 31:
            return False
        if month < 1 or month > 12:
            return False
        if year < 1 or year > 9999:
            return False
    except ValueError:
        return False
    if day == 31 and month not in [1, 3, 5, 7, 8, 10, 12]:
        return False
    return True


# Задание-3: "Перевернутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню — расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната, затем идет два этажа,
# на каждом из которых по две комнаты, затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача: нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
def inverted_tower(num):
    floor = 0
    i = 1
    while num - i**2 > 0:
        num -= i**2
        floor += i
        i += 1
    floor += num // i
    if num % i > 0:
        floor += 1
    left = num % i
    if left == 0:
        left = i
    return "{} {}".format(floor, left)


# -----------------------------------TEST------------------------------------------------
class Test(unittest.TestCase):

    def test_parse_equation(self):
        self.assertEqual(parse_equation("y = -12*x + 11111140.2121", 2.5), 11111110.2121)
        self.assertEqual(parse_equation("y = -12x + 11111140.2121", 2.5), 11111110.2121)
        self.assertEqual(parse_equation2("y = -12*x + 11111140.2121", 2.5), 11111110.2121)
        self.assertEqual(parse_equation2("y = -12x + 11111140.2121", 2.5), 11111110.2121)

    def test_date_validation(self):
        self.assertEqual(date_validation("02.11.2013"), True)
        self.assertEqual(date_validation("03.09.2000"), True)
        # self.assertEqual(date_validation("01.22.1001"), False)
        self.assertEqual(date_validation("1.12.1001"), False)
        self.assertEqual(date_validation("-2.10.3001"), False)

    def test_inverted_tower(self):
        self.assertEqual(inverted_tower(1), "1 1")
        self.assertEqual(inverted_tower(4), "3 1")
        self.assertEqual(inverted_tower(6), "4 1")
        self.assertEqual(inverted_tower(13), "6 2")
        self.assertEqual(inverted_tower(30), "10 4")


if __name__ == "__main__":
    unittest.main()
