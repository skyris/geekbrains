import os

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (все выражение вводится целиком в виде строки)
# Вывод: 1 17/42 (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 2/3

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

class Person:
    def __init__(self, full_name, salary, job, time_rate):
        self.full_name = full_name
        self.salary = int(salary)
        self.job = job
        self.time_rate = int(time_rate)
        self.hours = None
        self.real_salary = None
    def add_hours(self, real_hours):
        self.real_hours = int(real_hours)
    def show_data(self):
        return "{0} {1} {2} {3} {4} {5}".format(self.full_name, self.job,
                                                self.salary, self.time_rate, self.real_hours, self.real_salary)
    def get_salary(self):
        self.salary_count()
        return self.real_salary
    def salary_count(self):
        addition = 0
        if self.real_hours > self.time_rate:
            addition = (self.salary / self.time_rate) * (self.real_hours - self.time_rate)
        self.real_salary = round((self.salary / self.time_rate) * self.real_hours + addition, 0)


def salary_counter():

    # Getting data from files
    cwd = os.getcwd()
    dir = os.path.join(cwd, "data")
    path_workers = os.path.join(dir, "workers")
    path_hours_of = os.path.join(dir, "hours_of")
    with open(path_workers, "r") as file:
       data = file.read().split("\n")[1:]
    with open(path_hours_of, "r") as file:
       hours = file.read().split("\n")[1:]

    # Uploading data
    staff = {}
    for line in data:
        line = line.split()
        full_name = " ".join(line[:2])
        staff[full_name] = Person(full_name, line[2], line[3], line[4])

    for line in hours:
        line = line.split()
        full_name = " ".join(line[:2])
        staff[full_name].add_hours(line[2])

    for i in staff:
        print(staff[i].show_data())
    print("--------------------------------------------------")
    for i in staff:
        staff[i].salary_count()

    for i in staff:
        print(staff[i].show_data())


salary_counter()

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
def sort_fruits():
    cwd = os.getcwd()
    fruits_txt_path = os.path.join(cwd, "data/fruits.txt")
    with open(fruits_txt_path, "r") as file:
        fruits_list = file.read().split("\n")
        fruits_list = sorted(list(filter(None, fruits_list)))

    rus_letters = map(chr, range(ord("А"), ord("Я")+1))
    fruits_dict = {}
    for letter in rus_letters:
        fruits_dict[letter] = []
    for fruit in fruits_list:
        fruits_dict[fruit[0]].append(fruit)

    res_dir = os.path.join(cwd, "data/res")
    if not os.path.exists(res_dir):
        os.makedirs(res_dir)

    for letter in fruits_dict:
        if len(fruits_dict[letter]):
            file_name = os.path.join(res_dir, "fruits_" + letter)
            with open(file_name, "w") as file:
                for item in fruits_dict[letter]:
                    file.write(item+"\n")

# sort_fruits()