import unittest
from contextlib import contextmanager

"""
def answerReturn():
    ans = input('enter yes or no')
    if ans == 'yes':
        return 'you entered yes'
    if ans == 'no':
        return 'you entered no'

"""
@contextmanager
def mockRawInput(mock):
    original_input = __builtins__.input
    __builtins__.input = lambda _: mock
    yield
    __builtins__.input = original_input


"""
class TestAnswerReturn(unittest.TestCase):
    def testYes(self):
        with mockRawInput('yes'):
            self.assertEqual(answerReturn(), 'you entered yes')

    def testNo(self):
        with mockRawInput('no'):
            self.assertEqual(answerReturn(), 'you entered no')

"""

def answer():
    ans = input('enter yes or no')
    if ans == 'yes':
        return 'you entered yes'
    if ans == 'no':
        return 'you entered no'



class PromiseString(str):
    def set(self, newString):
        self.innerString = newString
    def __eq__(self, other):
        return self.innerString == other

@contextmanager
def getPrint():
    promise = PromiseString()
    original_print = __builtins__.print
    __builtins__.print = lambda message: promise.set(message)
    yield promise
    __builtins__.print = original_print

class TestAnswer(unittest.TestCase):
    def testYes(self):
        with mockRawInput('yes'), getPrint() as response:
            answer()
            self.assertEqual(response, 'you entered yes')

    def testNo(self):
        with mockRawInput('no'), getPrint() as response:
            answer()
            self.assertEqual(response, 'you entered no')



# class PromiseString(str):
#     def set(self, newString):
#         self.innerString = newString
#
#     def __eq__(self, other):
#         return self.innerString == other
#
# @contextmanager
# def getPrint():
#     promise = PromiseString()
#     original_print = __builtins__.print
#     __builtins__.print = lambda message: promise.set(message)
#     yield promise
#     __builtins__.print = original_print











if __name__ == '__main__':
    unittest.main()