#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License"


# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class rel:
    """Types of relatives"""
    mother =      "mother"
    father =      "father"
    stepmother =  "stepmother"
    stepfather =  "stepfather"
    grandmother = "grandmother"
    grandfather = "grandfather"


class Person:

    def __init__(self, name):
        """name in format 'Surname Name Patronymic_name' """
        self.name = name

    def __str__(self):
        return self.name


class Student(Person):
    _all = {}

    def __init__(self, name):
        super().__init__(name)
        self.class_ = None
        self.relatives = {}
        Student._all[name] = self

    def add_relative(self, name, relative):
        self.relatives[relative] = name

    def get_relatives(self):
        return ",\n".join("{}: {}".format(key, self.relatives[key]) for key in self.relatives) + "."

    def enroll_to_class(self, some_class):
        if some_class in SchoolClasses._all:
            for cur_class in SchoolClasses._all:
                if some_class == cur_class:
                    SchoolClasses._all[some_class].add_student(self)
        else:
            print("There is no such class number")

    def __str__(self):
        name_lst = self.name.split()
        return "{} {:.1}.{:.1}.".format(name_lst[0], name_lst[1], name_lst[2])


class Teachers(Person):
    subjects = []
    _all = {}

    def __init__(self, name, subject):
        if subject not in Teachers.subjects:
            if name not in Teachers._all:
                super().__init__(name)
                self.subject = subject
                Teachers.subjects.append(subject)
                Teachers._all[name] = self
            else:
                print("This teacher is already working in the school.")
        else:
            print("This school subject is already being taught.")

    def enroll_to_class(self, some_class):
        if some_class in SchoolClasses._all:
            for cur_num in SchoolClasses._all:
                if some_class == cur_num:
                    SchoolClasses._all[some_class].add_teacher(self)
        else:
            print("There is no such class number")

    def __str__(self):
        return "{}: {}".format(self.subject, self.name)

    def change_subject_to(self, other_subject):
        self.subject = other_subject

    @staticmethod
    def get_all():
        return ", ".join(Teachers._all) + "."


class SchoolClasses:
    _all = {}

    def __init__(self, number):
        if number not in SchoolClasses._all:
            self.number = number
            SchoolClasses._all[number] = self
            self.students = {}
            self.teachers = {}
            self.subjects = []
        else:
            print("This class is already in the School")

    @staticmethod
    def get_all_classes():
        return ", ".join(name for name in SchoolClasses._all) + "."

    def __str__(self):
        return self.number

    def add_teacher(self, some_teacher):
        if some_teacher.name not in self.teachers:
            self.teachers[some_teacher.name] = some_teacher
            self.subjects.append(some_teacher.subject)
        else:
            print("{} is already teaching in this class".format(some_teacher.name))

    def get_teachers(self):
        return ", ".join("{} ({})".format(name, self.teachers[name].subject) for name in self.teachers) + "."

    def add_student(self, some_student):
        if some_student.name not in self.students:
            self.students[some_student.name] = some_student
            some_student._class = self
        else:
            print("{} is already in this class".format(some_student.name))

    def get_students(self):
        return ", ".join(name for name in self.students) + "."

    def transfer_student(self):
        pass


def test():

    list_of_classes = ["7А", "8Б", "9В"]

    list_of_students = [
        ["Иванов Леонид Иванович", [("Иванова Мария Сергеевна", rel.mother),
                                    ("Иванов Андрей Евгеньевич", rel.father),
                                    ("Иванов Сергей Григорьевич", rel.grandfather)]],
        ["Искандаров Азамат Булатович", [("Искандаров Булат Азаматович", rel.father)]],
        ["Карклиньш Роберт Игоревич", [("Карклиньш Игорь Андреевич", rel.father)]],
        ["Комков Степан Алексеевич", [("Комков Алексей Степанович", rel.father),
                                      ("Комков Анна Андреевна", rel.father)]],
        ["Лафдал Аниса Ахмедовна", [("Лафдал Ахмед Арифович", rel.father)]],
        ["Лопатников Алексей Александрович", [("Лопатников Александр Андреевич", rel.father)]],
        ["Манжина Ольга Андреевна", [("Манжин Андрей Сергеевич", rel.father)]],
        ["Набиев Аблайхан Русланович", [("Набиева Марьям Халиловна", rel.mother)]],
        ["Полякова Екатерина Борисовна", [("Поляков Борис Борисович", rel.stepfather)]],
        ["Тимошинов Дмитрий Иванович", [("Тимошинов Иван Леонидович", rel.father)]],
        ["Толкачев Иван Павлович", [("Толкачева Зоя Дмитриевна", rel.mother)]],
        ["Трушина Кристина Андреевна", [("Трушин Алексей Николаевич", rel.grandfather)]]
    ]

    list_of_teachers = [
        ("Ломоносов Михаил Васильевич", "Physics"),
        ("Лобачевский Николай Иванович", "Math"),
        ("Менделеев Дмитрий Иванович", "Chemistry"),
        ("Прокофьев Сергей Сергеевич", "Music"),
    ]

    cls = SchoolClasses(list_of_classes[0])
    for row in list_of_students:
        student = Student(row[0])
        for r in row[1]:
            student.add_relative(r[0], r[1])
        cls.add_student(student)

    for teach in list_of_teachers:
        teacher = Teachers(teach[0], teach[1])
        cls.add_teacher(teacher)

    for other_class in list_of_classes[1:]:
        SchoolClasses(other_class)

    #----------------------------------------------------------------------
    # 1. Получить полный список всех классов школы
    print("-"*60)
    print(SchoolClasses.get_all_classes())

    # 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
    print("-"*60)
    print(SchoolClasses._all["7А"].get_students())

    # 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
    print("-"*60)
    print(Student._all["Искандаров Азамат Булатович"]._class.subjects)

    # 4. Узнать ФИО родителей указанного ученика
    print("-"*60)
    print(Student._all["Иванов Леонид Иванович"].get_relatives())

    # 5. Получить список всех Учителей, преподающих в указанном классе
    print("-"*60)
    print(SchoolClasses._all["7А"].get_teachers())


if __name__ == "__main__":
    test()
