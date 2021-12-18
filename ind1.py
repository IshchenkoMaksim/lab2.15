#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Написать программу, которая считывает текст из файла и выводит на экран только
предложения, не содержащие запятых.
"""


if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as f:
        content = f.read()

    for sentence in content.split('.'):
        if "," not in sentence:
            print(sentence)
