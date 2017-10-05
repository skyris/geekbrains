import random

#
# SAMPLE = range(1,91)
# lst = list(SAMPLE)
# def get_barrel(x):
#     random.shuffle(x)
#     yield x.pop(0)
#
#
# class Card:
#     def __init__(self, name):
#         self.numbers = random.sample(SAMPLE, 15)
#         self.name = name
#         self.list1 = self.numbers[:5]
#         self.list2 = self.numbers[5:10]
#         self.list3 = self.numbers[10:]
#         def build_line(lst):
#             res = ' '
#             lst_cur = sorted(lst)
#             for i in range(4):
#                 rand_place = random.randint(0, 9)
#                 lst_cur.insert(rand_place, " ")
#             return lst_cur
#
#         self.line1 = build_line(self.list1)
#         self.line2 = build_line(self.list2)
#         self.line3 = build_line(self.list3)
#         self.lines = (self.line1,  self.line2,  self.line3)
#         self.draw_card(self.lines)
#
#     def draw_card(self, lines):
#         print("---", "Карточка " + self.name + "а", "---")
#         for line in lines:
#             draw = ''
#             for i in line:
#                 draw += str(i) + ' '
#             print(draw)
#         print("--------------------------")
#
#     def check_turn(self, turn):
#         for line in self.lines:
#             if turn in line:
#                 place = line.index(turn)
#                 line[place] = '-'
#                 print(turn, "Совпало!!!!!!!")
#         self.draw_card(self.lines)
#
#
# class Player:
#     def __init__(self, name):
#         self.name = name
#
#
#     def make_turn(self):
#        self.turn = next(get_barrel(lst))
#        print(self.name, 'вытянул ', self.turn)
#        c2.check_turn(self.turn)
#     '''
#     def cross_or_cont(self):
#         des = input("Введите З чтобы зачеркнуть или П чтобы продолжить")
#         if des == 'З':
#             if self.turn in self.numbers:
#                 pass
#     '''
#
# player1 = "Игрок"
# player2 = "Компьютер"
# c1 = Card(player1)
# c2 = Card(player2)
# p1 = Player(player1)
# p2 = Player(player2)
# p1.make_turn()
# c1.check_turn(p1.turn)
# p2.make_turn()
# c2.check_turn(p2.turn)


#-------------------------------------------------------------------

#
# SAMPLE = range(1,91)
# lst = list(SAMPLE)
# def get_barrel(x):
#     random.shuffle(x)
#     yield x.pop(0)
#
#
# class Card:
#     def __init__(self, name):
#         self.numbers = random.sample(SAMPLE, 15)
#         self.name = name
#         self.list1 = self.numbers[:5]
#         self.list2 = self.numbers[5:10]
#         self.list3 = self.numbers[10:]
#         def build_line(lst):
#             res = ' '
#             lst_cur = sorted(lst)
#             for i in range(4):
#                 rand_place = random.randint(0, 9)
#                 lst_cur.insert(rand_place, " ")
#             return lst_cur
#
#         self.line1 = build_line(self.list1)
#         self.line2 = build_line(self.list2)
#         self.line3 = build_line(self.list3)
#         self.lines = (self.line1,  self.line2,  self.line3)
#         self.draw_card(self.lines)
#
#     def draw_card(self, lines):
#         print("---", "Карточка " + self.name + "а", "---")
#         for line in lines:
#             draw = ''
#             for i in line:
#                 draw += str(i) + ' '
#             print(draw)
#         print("--------------------------")
#
#     def check_turn(self, turn):
#         print("вызываю check_turn у объекта  ", self.name)
#         for line in self.lines:
#             if turn in line:
#                 place = line.index(turn)
#                 line[place] = '-'
#                 print(turn, "Совпало!!!!!!!")
#         self.draw_card(self.lines)
#
#
# class Player:
#     def __init__(self, name):
#         self.name = name
#
#
#     def make_turn(self, some_card):
#        turn = next(get_barrel(lst))
#        print(self.name, 'вытянул ', turn)
#        some_card.check_turn(turn)
#     '''
#     def cross_or_cont(self):
#         des = input("Введите З чтобы зачеркнуть или П чтобы продолжить")
#         if des == 'З':
#             if self.turn in self.numbers:
#                 pass
#     '''
#
# player1 = "Игрок"
# player2 = "Компьютер"
# c1 = Card(player1)
# c2 = Card(player2)
# p1 = Player(player1)
# p2 = Player(player2)
# for i in SAMPLE:
#     p1.make_turn(c1)
#     p2.make_turn(c2)


SAMPLE = range(1,91)
lst = list(SAMPLE)
def get_barrel(x):
    random.shuffle(x)
    yield x.pop(0)


class Card:
    def __init__(self, name):
        self.numbers = random.sample(SAMPLE, 15)
        self.name = name
        self.list1 = self.numbers[:5]
        self.list2 = self.numbers[5:10]
        self.list3 = self.numbers[10:]
        def build_line(lst):
            res = ' '
            lst_cur = sorted(lst)
            for i in range(4):
                rand_place = random.randint(0, 9)
                lst_cur.insert(rand_place, " ")
            return lst_cur

        self.line1 = build_line(self.list1)
        self.line2 = build_line(self.list2)
        self.line3 = build_line(self.list3)
        self.lines = (self.line1,  self.line2,  self.line3)
        self.draw_card(self.lines)

    def draw_card(self, lines):
        print("---", "Карточка " + self.name + "а", "---")
        for line in lines:
            draw = ''
            for i in line:
                draw += str(i) + ' '
            print(draw)
        print("--------------------------")

    def check_turn(self, turn):
        print("вызываю check_turn у объекта  ", self.name)
        for line in self.lines:
            if turn in line:
                place = line.index(turn)
                line[place] = '-'
                print(turn, "Совпало!!!!!!!")
        self.draw_card(self.lines)


class Player:
    def __init__(self, name):
        self.name = name


    def make_turn(self, card, turn):

       print(self.name, 'вытянул ', turn, 'проверяет карту', card.name)
       card.check_turn(turn)
    '''
    def cross_or_cont(self):
        des = input("Введите З чтобы зачеркнуть или П чтобы продолжить")
        if des == 'З':
            if self.turn in self.numbers:
                pass
    '''

player1 = "Игрок"
player2 = "Компьютер"
p1 = Player(player1)
p2 = Player(player2)
c1 = Card(p1.name)
c2 = Card(p2.name)

for i in SAMPLE:
    turn = next(get_barrel(lst))
    p1.make_turn(c1,turn)
    p2.make_turn(c2,turn)