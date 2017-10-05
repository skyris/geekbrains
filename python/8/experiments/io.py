import unittest
from contextlib import contextmanager
from io import StringIO


@contextmanager
def mock_print():
    stream = StringIO()
    original_print = __builtins__.print
    __builtins__.print = lambda x: original_print(x, file=stream)
    yield stream
    __builtins__.print = original_print
    stream.close()


@contextmanager
def mock_input(value):
    """
    Контекстный менеджер "подделывающий" функцию input
    :param value: генератор ответов
    :return:
    """
    original_input = __builtins__.input
    __builtins__.input = lambda _: next(value)  # итерация по генератору
    yield
    __builtins__.input = original_input



def helper_for_gen(*args):
    """
    Решает задачу, когда нужно "подделать" несколько функций input
    :param args: ответы пользователя
    :return: генератор
    """
    for arg in args:
        yield arg


def swap():
    a = input("Введите a: ")
    b = input("Введите b: ")
    a, b = b, a  # Можно через tmp, но зачем...
    print("a={0}, b={1}".format(a, b))


def age_verification():
    while True:
        try:
            age = int(input("Введите Ваш возраст: "))
            break
        except ValueError:
            print("Введите возраст цифрами.")
    if age < 18:
        print("Извините, пользование данным ресурсом только с 18 лет")
    else:
        print("Доступ разрешен")



class TestWithMockingInputAndPrint(unittest.TestCase):

    def test_second_task_1(self):
        gen = helper_for_gen(80, 90)
        with mock_input(gen), mock_print() as stream:
            swap()
            self.assertEqual(stream.getvalue(), "a={0}, b={1}\n".format(90, 80))

    def test_second_task_2(self):
        gen = helper_for_gen(1, 2)
        with mock_input(gen), mock_print() as stream:
            swap()
            self.assertEqual(stream.getvalue(), "a={0}, b={1}\n".format(2, 1))

    def test_second_task_3(self):
        gen = helper_for_gen(10, 10)
        with mock_input(gen), mock_print() as stream:
            swap()
            self.assertEqual(stream.getvalue(), "a={0}, b={1}\n".format(10, 10))

    def test_third_task_young(self):
        gen = helper_for_gen("17")
        with mock_input(gen), mock_print() as stream:
            age_verification()
            self.assertEqual(stream.getvalue(), 'Извините, пользование данным ресурсом только с 18 лет\n')

    def test_third_task_18(self):
        gen = helper_for_gen("18")
        with mock_input(gen), mock_print() as stream:
            age_verification()
            self.assertEqual(stream.getvalue(), 'Доступ разрешен\n')

    def test_third_task_old(self):
        gen = helper_for_gen("59")
        with mock_input(gen), mock_print() as stream:
            age_verification()
            self.assertEqual(stream.getvalue(), 'Доступ разрешен\n')







if __name__ == "__main__":
    unittest.main()

