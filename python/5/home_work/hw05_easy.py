#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from difflib import context_diff
import shutil
import unittest


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License"


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def create_dirs(dirs):
    for dir in dirs:
        path = os.path.join(os.getcwd(), dir)
        if not os.path.exists(path):
            os.mkdir(path)


def remove_dirs(dirs):
    for dir in dirs:
        path = os.path.join(os.getcwd(), dir)
        if os.path.exists(path):
            shutil.rmtree(path)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_of_folders(path):
    dirs = []
    for item in os.listdir(path):
        if os.path.isdir(item):
            dirs.append(item)
    return sorted(dirs)


# one-liner with the same functionality
# print(sorted(filter(os.path.isdir, os.listdir(os.getcwd()))))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_current_file(new_name, *, force=False):
    path = os.path.join(os.getcwd(), new_name)
    if force or not os.path.exists(path):
        shutil.copy2(__file__, new_name)


def test_copy_current_file_unix(new_name):
    if os.name == "posix" and shutil.which("diff"):
        info = "".join(os.popen("diff {} {}".format(__file__, new_name)))
        return True if not info else info


def test_copy(new_name):
    with open(__file__) as current:
        with open(new_name) as copy:
            diff = "".join(context_diff(list(current), list(copy), fromfile=__file__, tofile=new_name))
    print(repr(diff))
    return diff

# ---------------------------------TEST----------------------------------


class Test(unittest.TestCase):
    dirs = list(map(lambda num: "dir_" + str(num), range(1, 10)))

    def test_create_dirs(self):
        create_dirs(self.dirs)
        self.assertTrue(all(filter(os.path.exists, self.dirs)))

    def test_list_of_folders(self):
        res = os.popen("ls -d */")
        self.assertCountEqual(list_of_folders(os.getcwd()), list(map(lambda dir: dir.rstrip("/\n"), res)))
        res.close()

    def test_remove_dirs(self):
        remove_dirs(self.dirs)
        self.assertTrue(not any(filter(os.path.exists, self.dirs)))

    def test_copy(self):
        new_name = "yet_another_copy.py"
        copy_current_file(new_name, force=True)
        with open(__file__) as current:
            with open(new_name) as copy:
                diff = "".join(context_diff(list(current), list(copy), fromfile=__file__, tofile=new_name))
        self.assertEqual(diff, "")


if __name__ == "__main__":
    unittest.main()
