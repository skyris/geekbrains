import unittest
import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


# Ход рассуждения был следующим:
# Вычиление ряда Фиббоначи рекурсией
# Из-за неоднократного вычисления одних и тех же значнний
# Сложность алгоритма О(2**n) - экспонента
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# Вычисление ряда Фибоначи рекурсией с использованием глобального словаря для
# уже найденных элементов. Та же самая сложность, но из-за мемоизации работает
# намного быстрее
mem = {0: 1, 1: 1}


def new_fib(n):
    if n not in mem:
        mem[n] = mem.get(n - 1, new_fib(n - 1)) + \
            mem.get(n - 2, new_fib(n - 2))


# Ряд фибоначи от n до m с использованием ООП
# Минус: ограничение по глубине рекурсии
class Fib:

    def __init__(self):
        self.mem = {0: 1, 1: 1}

    def get_interval(self, n, m):
        self.count(m)
        return sorted(self.mem.values())[n:m + 1]

    def count(self, n):
        if n not in self.mem:
            self.mem[n] = self.mem.get(n - 1,
                                       self.count(n - 1)) + self.mem.get(n - 2,
                                                                         self.count(n - 2))

# Ряд фибоначи от n до m с использованием замыкания
# Минус: ограничение по глубине рекурсии
# Рекурсию легко писать, но она не эффективна по памяти
# Интерпретатор питона ставит ограничение на глубину рекурсии.
# Можно поставить import sys; sys.setrecursionlimit(m+2)
# Но эффективней по памяти программа не будет


def fibonacci(n, m):
    mem = {0: 1, 1: 1}

    def fib(m):
        if m not in mem:
            return mem.setdefault(m - 1, fib(m - 1)) + \
                mem.setdefault(m - 2, fib(m - 2))

    fib(m)
    return sorted(mem.values())[n:m + 1]


#  TODO Ряд фибоначи от n до m динамическим программированием
#
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод
# sort()


# Учил раньше сортировки. Записал, то что вспомнил сразу.
# Сортировка пузырьком
# Поочередно сравниваем соседние элементы
# Если порядок нарушен - меняем местами.
def bubble_sort(lst):
    for end in range(len(lst), 1, -1):
        for i in range(1, end):
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]  # swap
    return lst

# TODO Сортировка слиянием
def merge_sort(lst):
    pass


# TODO Selection sort
# Селекшен сорт немного похожа на сортировку пузырьком,
# но в ней на каждом шаге ищем минимальное значение
# и ставим в конец ОТСОРТИРОВАННОГО списка
def selection_sort(lst):
    pass

# Быстрая сортировка
# Берем произвольный элемент за основу.
# Кажый элемент в зависимости от того, мешьше он основы
# или больше, помещаем до основы или после основы.
# Делаем это рекурсивно


def quick_sort(lst):
    """
    Quick sort using list comprehension.
    Pivot is first element of each list.
    """
    if lst:
        return quick_sort([x for x in lst if x < lst[0]]) + [x for x in lst if x == lst[0]] +\
            quick_sort([x for x in lst if x > lst[0]])
    return []


# sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def filtr2(foo, seq):
    if type(foo) == type(lambda _: _):
        return (x for x in seq if foo(x))
    elif foo is None:
        return (x for x in seq if x)


# Постарался сделать максимально похоже:
# 1) в filter можно впихнуть None вместо функции
# 2) на выходе генератор


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def is_parallelogram(a, b, c, d):
    return distance(a, b) == distance(c, d) and distance(b, c) == distance(a, d)


def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# ------------------------------------TEST---------------------------------------------
class Test(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(0), 1)
        self.assertEqual(fib(2), 2)
        self.assertEqual(fib(3), 3)
        self.assertEqual(fib(4), 5)
        self.assertEqual(fib(10), 89)

    def test_quick_sort(self):
        self.assertEqual(quick_sort([2, 10, -12, 2.5, 20, -11, 4, 4, 0]), sorted([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
        self.assertEqual(bubble_sort([2, 10, -12, 2.5, 20, -11, 4, 4, 0]), sorted([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

    def test_filtr(self):
        seq = [1, 2, -3, 0, 8, -7, 6, None]
        foo =  lambda x: x > 0
        self.assertEqual(list(filtr2(foo, seq)), list(filter(foo, seq)))
        self.assertEqual(list(filtr2(None, seq)), list(filter(None, seq)))

    def test_is_parallelogram(self):
        self.assertEqual(is_parallelogram((0,0),(0,10),(10,10),(10,0)), True)
        self.assertEqual(is_parallelogram((0,0),(10,0),(10,10),(0,10)), True)
        self.assertEqual(is_parallelogram((0,0),(5,1),(6,6),(1,5)), True)
        self.assertEqual(is_parallelogram((0,1),(0,10),(10,10),(10,0)), False)


if __name__ == "__main__":
    unittest.main()
