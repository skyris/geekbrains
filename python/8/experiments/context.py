# with open("newfile.txt", "w", encoding="utf-8") as g:
#     d = int(input(">"))
#     print('1 / {} = {}'.format(d, 1 / d), file=g)

#
# class Hello(object):
#     def __init__(self):
#         print("created")
#     def __del__(self):
#         print("destructor")
#     def __enter__(self):
#         print("enter")
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("exit")
#
#
#
# with Hello():
#     print("my code")



import contextlib

@contextlib.contextmanager
def bold_text():
    print('<b>', end="")
    yield # код из блока with выполнится тут
    print('</b>')

with bold_text():
    print("Hello, World", end="")