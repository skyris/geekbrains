#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Вынимающий и выкрикивающий числа делает это независимо от двух игроков.
Если игроки успели выбрать - хорошо, не успели - их проблема.
Игра заканчивается тогда, когда 1) кто-то первый вышел или тогда когда 2) кончились все числа у выкрикивающего. 
В случае (2) подсчитываем число оствшиеся числа у игроков. У кого меньше осталось, тот и выиграл.

"""
import asyncio
from itertools import islice
from random import randint
import os
import sys
from color import Color, color_print
import non_blocking_input as nb


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License"


"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
rnd_ball_iter = None
my_card = None
comp_card = None
asked_flag = False
resp = None

end_of_round = False

class RandomNumberGenerator:
    def __init__(self, start, end):
        self.row = list(range(start, end+1))

    def __iter__(self):
        return self

    def __next__(self):
        if self.row:
            p = randint(0, self.items_left()-1)
            return self.row.pop(p)
        else:
            raise StopIteration

    def items_left(self):
        return len(self.row)


def matrix_view(matrix):
    return "\n".join(" {:>2} {:>2} {:>2} {:>2} {:>2}"
                     " {:>2} {:>2} {:>2} {:>2}".format(*row) for row in matrix)


def show_all(my_mat, comp_mat, ball, balls_left):
    if os.name == "nt":
        os.system("cls")   # Clear screen
    else:
        os.system('clear')
    color_print("Новый бочонок: {} (осталось {})".format(ball, balls_left), color=Color.White)
    color_print("--- Карточка компьютера ---", color=Color.BGreen)
    color_print(matrix_view(comp_mat), color=Color.Blue)
    color_print("---------------------------", color=Color.BGreen)
    color_print("------ Ваша карточка ------", color=Color.BGreen)
    color_print(matrix_view(my_mat), color=Color.Cyan)
    color_print("---------------------------", color=Color.BGreen)
    color_print("Зачеркнуть цифру? (y/n) ", color=Color.Yellow)


class Card:
    def __init__(self):
        matrix = [['', '', '', '', '', '', '', '', ''],
                  ['', '', '', '', '', '', '', '', ''],
                  ['', '', '', '', '', '', '', '', '']]
        numbers_iter = RandomNumberGenerator(1, 90)
        for row in range(3):
            numbers = sorted(islice(numbers_iter, 5))
            places = sorted(islice(RandomNumberGenerator(0, 8), 5))
            for pl, val in zip(places, numbers):
                matrix[row][pl] = val
        self.content = matrix

    def change(self, digit):
        for row_num, row in enumerate(self.content):
            for col_num, val in enumerate(row):
                if digit == val:
                    self.content[row_num][col_num] = "-"

    def contains(self, digit):
        return digit in [val for row in self.content
                                    for val in row]

    def items_left(self):
        count = 0
        for row in self.content:
            for item in row:
                if isinstance(item, int):
                    count += 1
        return count


def you_fail():
    color_print("Вы проиграли!", color=Color.Red)
    sys.exit()


def you_win():
    color_print("Вы выиграли!", color=Color.BGreen)
    color_print("Компьютер проиграл!", color=Color.BGreen)
    sys.exit()


def dead_heat():
    color_print("Ничья.", color=Color.IYellow)
    sys.exit()



async def leader():
    global rnd_ball_iter, my_card, comp_card
    rnd_ball_iter = RandomNumberGenerator(1, 90)
    my_card = Card()
    comp_card = Card()
    # Пока остались бочонки и у меня и у компа остались карты
    while rnd_ball_iter.items_left() and my_card.items_left() and comp_card.items_left():
        rnd_ball = next(rnd_ball_iter)
        show_all(my_card.content, comp_card.content, rnd_ball, rnd_ball_iter.items_left())
        await asyncio.sleep(3)
        global end_of_round
        end_of_round = True
        if os.name == "nt":
            os.system("cls")   # Clear screen
        else:
            os.system('clear')
        color_print(repr(resp), color=Color.Yellow)
        await asyncio.sleep(5)
        # global resp
        # resp = None
        
        # global asked_flag
        # asked_flag = True

async def test():
    a = None
    while True:
        print("Test--------{}".format(a))
        await asyncio.sleep(0.1)
        
        #a = input("Блокирующий инпут") #Блокирует ВСЕ
        #Блокируемся и не идем дальше В ДАННОЙ КОРУТИНЕ если не нажали ничего
        # Нужно по таймауту переходить на следующую строку кода 
        # a = await nb.async_input("Get data===>")
        # print("{}".format(a))

async def player():   
        global resp
        resp = None
        while True:
            if resp.lower() == "y":
                    resp = True
            elif resp.lower() == "n":
                resp = False
            else:
                print("suck")
                res = None
                # resp = await nb.async_input("Get data===>")

            # print(resp)
        # global asked_flag
        # asked_flag = False
        # while not asked_flag or (resp.lower() != "n" and resp.lower() != "y"):
        #     asked_flag = True
        #     resp = input("")
        # if resp.lower() == "y":
        #     resp = True
        # elif resp.lower() == "n":
        #     resp = False
"""
        contains = my_card.contains(rnd_ball)
        if resp != contains:
            you_fail()
        if contains:
            my_card.change(rnd_ball)
        if comp_card.contains(rnd_ball):
            comp_card.change(rnd_ball)

    if my_card.items_left() > comp_card.items_left():
        you_fail()
    elif my_card.items_left() < comp_card.items_left():
        you_win()
    else:
        dead_heat()

"""

loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(leader()),
    asyncio.ensure_future(test()),
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# if __name__ == "__main__":
#     game()


# # TODO ---------------------------
# def comp_looser():

#     # TODO curses?
#     # TODO comp is inattentive

#     if randint(range(0,200)) == 0:
#         you_win()
