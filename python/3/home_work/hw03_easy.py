# 1/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License;)"


# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math


def my_round(number, ndigits):
    if not (isinstance(ndigits, int) and (isinstance(number, float) or isinstance(number, int))):
        raise TypeError
    try:
        num = str(number).split(".")
        end = num[1][:ndigits]
        if len(end) < ndigits:
            return number
        end = int(end)
        if int(num[1][ndigits]) > 4:
            end += 1
        # print(ndigits, end)
        # print(10**ndigits)
        # print(end / (10**ndigits))
        end = end / 10**ndigits
        return float(num[0]) + end
    except IndexError:
        return number
    except ValueError:
        raise TypeError("Not a number")


def my_round2(number, ndigits):
    if not (isinstance(ndigits, int) and (isinstance(number, float) or isinstance(number, int))):
        raise TypeError
    num = str(float(number))
    zero_place = num.find(".")


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
def lucky_ticket(ticket_number):
    num = str(ticket_number)
    return sum(map(int, num[:len(num) // 2])
               ) == sum(map(int, num[len(num) // 2:]))


class Test(unittest.TestCase):

    def test_my_round(self):
        self.assertEqual(my_round(2.4444, 2), 2.44)
        self.assertEqual(my_round(3.99999, 3), 4.0)
        self.assertEqual(my_round(2.1234567, 5), 2.12346)
        self.assertEqual(my_round(2.1234567, 0), 2.0)

    def test_lucky_ticket(self):
        self.assertEqual(lucky_ticket(123321), True)
        self.assertEqual(lucky_ticket(123321), True)
        self.assertEqual(lucky_ticket(123327), False)


if __name__ == "__main__":
    unittest.main()
