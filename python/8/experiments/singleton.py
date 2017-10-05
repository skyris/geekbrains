
# Decorator Singleton
def singleton(cls):
    instances = {}
    def getinstance():
        instances.setdefault(cls, cls())
        return instances[cls]
    return getinstance


@singleton
class MyClass:
    def __init__(self):
        print("I was born!")
    def __del__(self):
        print("I'm dying")


MyClass = singleton(MyClass)
MyClass()


# Decorator Counter
def counter(foo):
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(count)
        foo()
    return inner

# Decorator Counter 2
def counter2(foo):
    def inner():
        foo()
        inner.plus += 1
        print(inner.plus)
    inner.plus = 0
    return inner



# Создание "ячейки" в которую можно положить гетом и получить значение сетом
def cell(value=None):
    def get():
        return value
    def set(update):
        nonlocal value
        value = update
    return get, set


get, set = cell()

set(60)
print(get())