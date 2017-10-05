from functools import reduce
import itertoolitertools
    

class Color:
    def __init__(self, ):
        self.colors = [0, 1, 2, 3, 4, exec("raise StopIteration") , 5, 6, 7]
    def __iter__(self):
        i = 0
        while True:
            yield self.colors[i]
            i += 1
            if i == len(self.colors):
                i = 0



class Color:
    def __init__(self, ):
        self.colors = [0, 1, 2, 3, 4, 5, 6]
        i = 0
    def __iter__(self):
        return self
        while True:
            yield self.colors[i]
            i += 1
            if i == 5:
                raise StopIteration




class B:
    def __init__(self, ):
        self.inner = [0, 1, 2, 3, 4, 5, 6]
        self.i = 0
    # def __iter__(self):
    #     return self
    def __next__(self):
        if self.i == 5:
            raise StopIteration
        self.i += 1
        return self.inner[self.i-1]



class Enum:
    def __init__(self, inner):
        self.inner = inner
        self.num = list(range(len(inner)))
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < len(self.inner):
            self.i +=1
            return self.num[self.i-1], self.inner[self.i-1]
        else:
            raise StopIteration


class A:
    def __init__(self):
        self.inner = list(range(10))
    def __call__(self, *args, **kwargs):   # <-- функция генераторы
        i = 0
        while True:
            yield self.inner[i]
            i += 1
            if i == len(self.inner):
                i = 0



class Foo(list):
    def __init__(self):
        self.inner = list(range(10))
    def __contains__(self, item):
        return item in self.inner
    def __call__(self, *args, **kwargs):
        return self.inner[args[0]]




class with_next:
    l = [1,2,3,4,5]
    def __next__(self):
        return  10

w = with_next()

class Foo:
    def __init__(self):
        self.inner  = [1,2,3,4,5]
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        try:
            self.i = self.i + 1
            return  self.inner[self.i - 1]
        except IndexError:
            raise StopIteration



class From_Datchik:
    def __init__(self):
        self.buffer = []
    def __iter__(self):
        return self
    def __next__(self):
        return self.buffer.pop(0)
    def get_data(self):
        self.buffer.append("from_source")

"""
Про генераторы сейчас лекцию смотрю. К примеру надо обработать данные, идущие от датчика.
Создаем класс - генератор с буфером, такой чтобы синхронно брать с одной сторон из этого буфера next-ом
и параллельно асинхронно
пишем в его конец. Чет туплю, а как асинхронно писать в как
"""

"""
Метод iter возвращает генератор через yield, а у самого генератора есть метод next
по генератору можно пройтись только один раз. После этого генератор будет указывать на свой последний элемент.
В этом отличие от списка. сам объект списка просто хранит элементы
Цикл у объекта получает итератор и потом цикл работает не с самим объектом, а с его итератором
itertools
"""


import itertools
itertools.chain([1,2,3,4], "abcsd") - объединяет два разных итератора
itertools.count(10) - начинает с заданного числа и считает до бесконечности
itertools.cycle("12345") - бесконечно повторяет заданную последовательность

a = itertools.chain([1,2,3,4], "abcsd")
next(a)

def get_largest_multiple(str_long_number):
    str_long_number = ''.join(number for number in str_long_number if number.isalnum())
    str_numbers = (str_long_number[x:x + 5] for x in range(len(str_long_number) - 4))
    multiply_nums = lambda x, y: int(x) * int(y)

    largest_multiple_numbers = max(str_numbers, key=lambda number: reduce(multiply_nums, number))
    index = str_long_number.find(largest_multiple_numbers)
    return (index, reduce(multiply_nums, largest_multiple_numbers))


def foo():
    global number
    number = number.replace("\n", "")
    lst = []
    for i in range(1000-5+1):
        multiply = reduce(lambda x, y: x * y, map(int, number[i:i+5]))
        lst.append([multiply, i])
    new = sorted(lst, key=lambda x: x[0])
    print("Наибольшее произведение - {}, индекс смещения первого числа последовательноси - {}"
          .format(new[-1][0], new[-1][1]))



def itemgetter(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g

f = itemgetter(5)
f(b) -> b[5]

func = lambda x,y: x*y
seq  = list(range(1,6))
reduce(func, seq)

def reduce(func, seq):
    if len(seq) == 2:
        return func(*seq)
    return func(seq[0], reduce(func, seq[1:]))

s = [1,2,3,4,5]
list(map(lambda x: x==4, s))




def map(func, iterable, *rest):
    for args in zip(iterable, *rest):
        yield func(*args)






class Identity:
    def __getitem__(self, idx):
        if idx > 5:
            raise IndexError(idx)
        return idx*2




class Rude:
    def __getitem__(self, item):
        print("fuck", item)


















