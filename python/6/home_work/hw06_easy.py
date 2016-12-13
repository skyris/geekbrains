#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import unittest


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License"


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Polygon:
    def __init__(self, *args, num_of_sides=3):
        self.num_of_sides = num_of_sides
        assert len(args) == self.num_of_sides, "Invalid number of vertices" # число вершин
        assert all(map(lambda dot: len(dot)==2, args)), "Wrong structure of the input data for vertices"
        assert all(map(lambda coord: isinstance(coord, (int, float)), (coord for dot in args for coord in dot))), \
            "Wrong data type"
        self.vertices = args
        res = []
        angle = []
        for dot_one, dot_two in zip(self.vertices, self.vertices[1:] + self.vertices[:1]):
            cur_dist = self.dist(dot_one, dot_two)
            res.append(cur_dist)
            angle.append((dot_two[0] - dot_one[0]) / cur_dist)  # cosine angle of each side
        self.len_of_sides = tuple(res)
        self.angles_of_sides = tuple(angle)

    def dist(self, dot_one, dot_two):
        return math.sqrt((dot_two[0] - dot_one[0]) ** 2 + (dot_two[1] - dot_one[1]) ** 2)

    def perimeter(self):
        return sum(self.len_of_sides)

    def area(self):
        raise NotImplementedError



class Triangle(Polygon):
    def __init__(self, *args):
        super().__init__(*args)

    def heights(self):
        """Heights of triangle in the order of vertices"""
        res = []
        area = self.area()
        for length in self.len_of_sides:
            res.append(2 * area / length)
        return tuple(res[1:]+res[:1])

    def area(self):
        """Heron's Formula"""
        s = (self.perimeter())/2
        return math.sqrt(s * (s - self.len_of_sides[0]) *
                         (s - self.len_of_sides[1]) * (s - self.len_of_sides[2]))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.


class Quadrangle(Polygon):
    def __init__(self, *args):
        super().__init__(*args, num_of_sides=4)


class Trapezoid(Quadrangle):
    def __init__(self, *args):
        super().__init__(*args)
        # does in have two parallel sides
        assert self.angles_of_sides[0] == -self.angles_of_sides[2] or\
               self.angles_of_sides[1] == -self.angles_of_sides[3], "This quadrangle is not a trapezoid"

    def area(self):
        if self.angles_of_sides[0] == -self.angles_of_sides[2]:
            base0 = self.len_of_sides[0]
            base1 = self.len_of_sides[2]
            height = Triangle(self.vertices[0], self.vertices[2], self.vertices[3]).heights()[0]
        else:
            base0 = self.len_of_sides[1]
            base1 = self.len_of_sides[3]
            height = Triangle(self.vertices[1], self.vertices[3], self.vertices[0]).heights()[0]

        # Может служить примером плохой реализация метода, поскольку привязываюсь к классу Triangle.
        # Класс получается не автоновным и в случае его импортирования в другой модуль,
        # без неочевидного импорта класса Triangle, работать не будет.
        # Это был "хак" для того, чтобы быстро и без тригонометрии посчитать высоту трапеции.
        # А в принципе есть способ обратиться к классу яляющемуся потомком общего предка с моим классом?
        # Так сказать "кузину".

        return (base0 + base1) * height / 2

    @property
    def is_isosceles_trapezoid(self):
        return self.len_of_sides[0] == self.len_of_sides[2] or\
               self.len_of_sides[1] == self.len_of_sides[3]


class Test(unittest.TestCase):

    def test_triangle(self):
        # ассертами внутри класса проверяю пользовательский ввод
        # проверю правильно ли мои ассерты отлавливают неверный пользовательский ввод
        # Дал заведомо неверный пользовательский ввод и проверяю, что ассерты его отловили
        # Смотрю срабатывает ли проверка валидности входящих данных
        with self.assertRaisesRegex(AssertionError, "Invalid number of vertices"):
            Triangle((3, 4), (5, 6))

        with self.assertRaisesRegex(AssertionError, "Wrong structure of the input data for vertices"):
            Triangle((9,), (3, 4), (5, 6))

        with self.assertRaisesRegex(AssertionError, "Wrong data type"):
            Triangle((9, "9"), (3, 4), (5, 6))

        # Проверяю работу различных частей класса:
        triangle = Triangle((0, 0), (4, 3), (4, 0))
        self.assertEqual(triangle.len_of_sides, (5.0, 3.0, 4.0))
        self.assertEqual(triangle.angles_of_sides, (0.8, 0.0, -1.0))
        self.assertEqual(triangle.perimeter(), 12)
        self.assertEqual(triangle.area(), 6.0)
        self.assertEqual(triangle.heights(), (4.0, 3.0, 2.4))

    def test_trapezoid(self):
        with self.assertRaisesRegex(AssertionError, "Invalid number of vertices"):
            Trapezoid((3, 4), (5, 6))

        with self.assertRaisesRegex(AssertionError, "This quadrangle is not a trapezoid"):
            Trapezoid((0, 0), (2, 5), (6, 8), (9, 0))

        trapeze2 = Trapezoid((0, 0), (1, 4), (5, 4), (6, 0))
        self.assertTrue(trapeze2.is_isosceles_trapezoid)

        trapeze = Trapezoid((0, 0), (2, 5), (6, 5), (9, 0))
        self.assertFalse(trapeze.is_isosceles_trapezoid)
        self.assertAlmostEqual(trapeze.perimeter(), 24.2161167)
        self.assertAlmostEqual(trapeze.area(), 32.5)




if __name__ == "__main__":
    unittest.main()
