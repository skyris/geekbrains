#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmd
import os
import socket
from hw05_easy import list_of_folders, create_dirs, remove_dirs


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License"

# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций, и импортированные в данный файл из easy.py


# Поменял ТЗ. Было интересно разобраться с модулем cmd
# Сделал мини оболочку с несколькими unix-подобными командами


class Shell(cmd.Cmd):
    current_dir = os.getcwd()
    intro = "Welcome to our cozy tiny shell.\n" \
            "Little shell with bash flavor.\n" \
            "Type man, help or ? to list commands.\n"
    try:
        user = os.getlogin()
        host = socket.gethostname()
    except Exception:
        user = "User"
        host = "LocalHost"
    prompt = "{}@{} ~ {} > ".format(user, host, current_dir)

    def do_man(self, arg):
        "man - alias for standard help command"
        self.do_help(arg)

    def do_pwd(self, arg):
        "pwd - print name of current/working directory"
        print(self.current_dir)

    def do_cd(self, arg):
        "cd - change the current working directory"
        if not arg.startswith("/"):
            next_dir = os.path.join(self.current_dir, arg)
        else:
            next_dir = arg
        next_dir = os.path.normpath(next_dir)
        try:
            os.chdir(next_dir)
            self.current_dir = next_dir
        except FileNotFoundError:
            print("There is no such directory: {}".format(arg))
        self.prompt = "{}@{} ~ {} > ".format(self.user, self.host, self.current_dir)

    def do_ls(self, arg):
        "ls - list current directory folders"
        if not arg.startswith("/"):
            dir_to_watch = os.path.join(self.current_dir, arg)
        else:
            dir_to_watch = arg
        res = list_of_folders(dir_to_watch)
        if not res:
            res = "This directory does not have folders"
        print(res)
    def do_mkdir(self, arg):
        "mkdir - make directories"
        if arg:

            if arg.startswith("/"):
                paths = arg.split()
            else:
                args = arg.split()
                paths = list(map(lambda x: os.path.join(self.current_dir, x), args))

            create_dirs(*paths)
        else:
            print("Name of a new directory was not set.")
    def do_rmdir(self, arg):
        "rm - remove directories (empty or nonempty)"
        if arg:

            if arg.startswith("/"):
                paths = arg.split()
            else:
                args = arg.split()
                paths = list(map(lambda x: os.path.join(self.current_dir, x), args))

            remove_dirs(*paths)
        else:
            print("Name of folder to delete was not set.")

    def do_exit(self, arg):
        "Close the window, and exit shell"
        print('Thank you for using tiny shell')
        return True

# TODO Color parts of the text
# TODO Add autocomplete for arguments of commands


if __name__ == "__main__":
    Shell().cmdloop()
