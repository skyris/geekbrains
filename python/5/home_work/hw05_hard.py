#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import shutil


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License"


# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории



#        Victor Klimov:
#        И в unix и windows полный путь показывает команда pwd - print working directory.
#        Команда ls показывает содержимое директории.


# путь считать абсолютным (full_path) - в Linux начинается с /, в Windows с имени диска
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь. Исходной директорией считать ту,
# в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.



# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("rm <file> - удаляет файл или папку")
    print("cp <name> <name2> - копирует файл")
    print("cd <dir> - меняет текущую директорию")
    print("pwd - указывает текущий путь")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def remove_file():
    resp = input("Вы уверены? (y/N) ")
    if resp.lower().startswith("y"):
        if os.path.isdir(dir_name):
            shutil.rmtree(dir_name)
        else:
            os.remove(dir_name)


def copy_file():
    if not another_name:
        print("Необходимо указать файла вторым параметром новое имя файла третьим")
    shutil.copy2(dir_name, another_name)
    print("Файл {} скопирован".format(dir_name))


def print_cwd():
    print(os.getcwd())


def change_dir():
    os.chdir(dir_name)
    print(os.getcwd())
    #  Внутри рантайма мы меняем директорию, но когда интерпретатор заканчивает работу,
    #  вновь оказываемся в директории, из которой вызывался скрипт.
    #  Как сдалать чтобы оказывать в указанной директории, и можно ли сделать вообще пока не понял.
    #  Прокомментриуйте, пожалуйста.


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "rm": remove_file,
    "cp": copy_file,
    "pwd": print_cwd,
    "cd": change_dir
}
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    another_name = sys.argv[3]
except IndexError:
    another_name = None


try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
