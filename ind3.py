#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, использующую модуль os, которая будет
подменять время изменения файла, переданного командной строке
"""

import os
import sys
import time


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Передайте командной строке в качестве аргумента имя файла", file=sys.stderr)
        sys.exit(1)

    try:
        f = sys.argv[1]
        atime = os.stat(f).st_atime
        mtime = os.stat(f).st_mtime
        print("Старое время:", time.ctime(atime), time.ctime(mtime))

        delta = float(input("Введите разницу (в секундах): "))
        new_atime = atime - delta
        new_mtime = mtime - delta
        os.utime(f, times=(new_atime, new_mtime))
        atime = os.stat(f).st_atime
        mtime = os.stat(f).st_mtime
        print("Новое время:", time.ctime(atime), time.ctime(mtime))

    except IOError:
        print("Ошибка доступа к файлу", file=sys.stderr)
