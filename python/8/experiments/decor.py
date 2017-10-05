import functools
import sys

# Декоратор позволяет испольнить декорированный код только один раз
def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            inner.called = True
            return func(*args, **kwargs)
    inner.called = False
    return inner




def trace(foo):
    def inner(*args, **kwargs):
        print(foo.__name__, args, kwargs)
        return foo(*args, **kwargs)
    return inner


@trace
def identity(x):
    print("I do nothing useful")
    return x

identity(42)



def date_validation0(foo):
    def inner(date):
        date_list = date.split(".")
        if tuple(map(len, date_list)) != (2, 2, 4):
            return False
        try:
            day = int(date_list[0])
            month = int(date_list[1])
            year = int(date_list[2])
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
        return foo(date)
    inner.__name__ = foo.__name__
    inner.__doc__ = foo.__doc__
    inner.__module__ = foo.__module__
    return inner


date_validation_enabled = False


def date_validation(foo):
    @functools.wraps(foo)
    def inner(date):
        date_list = date.split(".")
        if tuple(map(len, date_list)) != (2, 2, 4):
            return False
        try:
            day = int(date_list[0])
            month = int(date_list[1])
            year = int(date_list[2])
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
        return foo(date)
    return inner if date_validation_enabled else foo





@date_validation
def date_to_text(date):
    date_list = date.split(".")
    month_dict = {
        1:"января", 2:"февраля", 3:"марта", 4:"апреля", 5:"мая", 6:"июня",
        7:"июля", 8:"августа", 9:"сентября", 10:"октября", 11:"ноября", 12:"декабря"
        }
    day_dict = {
        1:"первое", 2:"второе", 3:"третье", 4:"четвертое", 5:"пятое", 6:"шестое",
        7:"седьмое", 8:"восьмое", 9:"девятое", 10:"десятое", 11:"одинадцатое", 12:"двенадцатое",
        13:"тринадцатое", 14:"четырнадцатое", 15:"пятнадцатое", 16:"шестнадцатое", 17:"семнадцатое",
        18:"восемнадцатое", 19:"девятнадцатое", 20:"двадцатое", 21:"двадцать первое", 22:"двадцать второе",
        23:"двадцать третье", 24:"двадцать четвертое", 25:"двадцать пятое", 26:"двадцать шестое",
        27:"двадцать седьмое", 28:"двадцать восьмое", 29:"двадцать девятое", 30:"тридцатое", 31:"тридцать первое"
        }
    return "{} {} {} года".format(day_dict[int(date_list[0])], month_dict[int(date_list[1])], date_list[2] )




date_to_text("02.11.2013")