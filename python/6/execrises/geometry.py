# -*- coding: utf-8 -*-

"""
Это пример небольшой программы для рисования кругов и квадратов.
Вам нужно на основе этой программы сделать небольшую "танцевальную" сценку с
использованием кругов, квардратов и треугольников. Сделать всё это нужно в
объектно ориентированном стиле.

Какие классы нужно реализовать:

-Многоугольник(на его основе сделать квадрат и правильный треугольник)
--класс должен уметь отрисовывать себя
--перемещаться в некоторм направлении, заданом координатами x, y
--увеличивать(необязательно)
--поворачивать(необязательно)

-Квардрат(наследуется от многоугольника)
--метод __init__ принимает координаты середины, ширину и цвет

-Треугольник(наследуется от многоугольника)
--метод __init__ принимает координаты середины, длинну грани и цвет

-Круг
--метод __init__ принимает координаты середины, радиус и цвет
--класс должен уметь отрисовывать себя
--премещаться в некоторм направлении, заданом координатами x, y
--увеличивать(необязательно)

Также рекомендуется создать вспомогательный сласс Vector для представления
точек на плоскости и различных операций с ними - сложение, умножение на число,
вычитание.


Из получившихся классов нужно составить какую-нибудь динамическую сцену.
Смотрите пример example.gif
"""

import turtle
import time
import random


def draw_rect(ttl):
    x = random.randint(-200, 200) #получаем случайные координаты
    y = random.randint(-200, 200)

    ttl.color('red')    # устанавливаем цвет линии
    ttl.penup()         # убираем "ручку" от холста, чтобы переместить в нужное место
    ttl.setpos(x, y)    # перемещаем на первую вершину
    ttl.pendown()       # опускаем ручку обратно
    ttl.goto(x + 50, y) # проводим линии для сторон четырёхугольника
    ttl.goto(x + 50, y + 50)
    ttl.goto(x, y + 50)
    ttl.goto(x, y)

def draw_circle(ttl):
    x = random.randint(-200, 200) #получаем случайные координаты
    y = random.randint(-200, 200)

    ttl.color('violet')     # устанавливаем цвет линии
    ttl.penup()             # убираем "ручку" от холста, чтобы переместить в нужное место
    ttl.setpos(x, y)        # перемещаем в "основание" - это будет самая низкая точка
    ttl.pendown()           # опускаем ручку обратно

    ttl.circle(25)          # рисуем круг радиуса 25



def main():

    turtle.tracer(0, 0) # устанавливаем все задержки в 0, чтобы рисовалось мгновенно
    turtle.hideturtle() # убираем точку посередине

    ttl = turtle.Turtle() # создаём объект черепашки для рисования
    ttl.hideturtle()      # делаем её невидимой

    while True:
        time.sleep(0.5) # засыпаем на полсекунды, чтобы увидеть что нарисовали
        ttl.clear()     # очищаем всё нарисованое ранее
        draw_rect(ttl)
        draw_circle(ttl)
        turtle.update() # т.к. мы сделали turtle.tracer(0, 0), нужно обновить экран, чтобы увидеть нарисованное

if __name__ == '__main__':
    main()
