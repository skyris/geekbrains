#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import unittest
import random
import os


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License;)"


# Задание-1:
# Вывести символы в нижнем регистре, которые окружают 1 или более символа в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'


def upper_surround(line):
       res = "".join((map((lambda x: " " if x == x.upper() else x), line)))
       return res.split()


def upper_surround_re(line):
    pattern = r"([a-z]+)"
    return re.findall(pattern,line)


# Задание-2:
# Вывести символы в верхнем регистре, которые окружают ровно два символа в нижнем регистре слева
# и два символа в верхнем регистре справа. Решить задачу двумя способами: с помощью re и без.
# Т.е. из строки "sGAMkgAYEOmHBSQs" нужно получить ['GAM', 'EO']
# "GAMkgAYEO -> kgAY (два маленьких символа слева, два больших символа справа)," \
# " они окружаются большими символами GAM и EO. Как-то так :)"


line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'


# Результаты работы поисковой функции search_pattern без использования ругулярного выражения
# отличается от результата работы функции search_pattern_re, ипользующей регулярное выражение.
# Приведу пример AAAAbbCCDDeeJJJJJ
# Первая функция найдет результаты [AAAA, DD] ,[CCDD, JJJJJ]
# Функция с ругулярным выражением только [AAAA, DD], а пару [CCDD, JJJJJ] пропустит,
# поскольку DD уже встретилось в предыдущей паре. Как писать регулярное выражение, способное повторить
# результат первой функции, я пока не знаю.


def search_pattern(line):
    result = []
    for i in range(4, len(line)-1):
        if line[i].isupper() and line[i - 1].isupper():  # два больших символа подряд
                if line[i - 2].islower() and line[i - 3].islower():  # два маленьких перед ними
                    inner = ["", ""]
                    if line[i + 1].isupper():  # правее паттерна
                        start = i + 1
                        end = i + 2
                        try:
                            while line[end - 1].isupper():
                                end += 1
                        except IndexError:
                            pass
                        inner[1] = line[start: end-1]
                    if line[i - 4].isupper():  # левее паттерна
                        start = i - 4
                        end = i - 3
                        try:
                            while line[start:end].isupper():
                                start -= 1
                        except IndexError:
                            pass
                        inner[0] = line[start+1: end]
                    result.append(inner)

    return list(filter(lambda x:x[0].isalnum() and x[1].isalnum(), result))


def search_pattern_re(line):
    pattern = r"([A-Z]+)[a-z]{2}[A-Z]{2}([A-Z]+)"
    res = re.findall(pattern, line)
    return list(filter(lambda x: x[0].isalnum() and x[1].isalnum(), res))


# Задача-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла) произвольными целыми
# числами, в результате в файле должно быть 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр в вышезаполненном файле.


def foo():
    file_name = "file"
    path = os.path.join(os.getcwd(), file_name)
    if os.path.exists(path):
        os.remove(path)
    with open(path, "a") as f:
        for i in range(2500):
            f.write(str(random.randint(0, 9)))

    with open(path, "r") as f:
        file = f.read()

    lst = [[file[0], 1, 0]]
    for i in range(1, len(file)):
        if file[i] == file[i-1]:
            lst[-1][1] += 1
        else:
            lst.append([file[i], 1, i])
    s = sorted(lst, key=lambda x: x[1])
    return "\nЦифра {0} встретилась {1} {2} подряд".format(s[-1][0], s[-1][1], digit_to_word(s[-1][1]))


def digit_to_word(digit):
    digit = str(digit)
    if digit[-1] in ["2", "3", "4"]:
        return "раза"
    return "раз"


# ------------------------------TEST----------------------------------------------


class Test(unittest.TestCase):
    def test_upper_surround(self):
        # compare results of two functions
        self.assertEqual(upper_surround(line), upper_surround_re(line))


if __name__ == "__main__":
    print("\n{}{}{}\n".format("-" * 40, "Task 1. Solution 1", "-" * 40))
    print(upper_surround(line))
    print("\n{}{}{}\n".format("-" * 40, "Task 1. Solution 2", "-" * 40))
    print(upper_surround_re(line))
    print("\n{}{}{}\n".format("-" * 40, "Task 2. Solution 1", "-" * 40))
    print(search_pattern(line_2))
    print("\n{}{}{}\n".format("-" * 40, "Task 2. Solution 2", "-" * 40))
    print(search_pattern_re(line_2))
    print("\n{}{}{}\n".format("-" * 40, "Task 3. Solution 1", "-" * 40))
    print(foo())

    unittest.main()
