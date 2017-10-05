#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License"


# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True
# Вопрос: Чему была равна переменная a, если точно известно, что её значение не изменялось?
a = float("Inf")

assert a == a**2
assert a == a*2
assert a > 999999
