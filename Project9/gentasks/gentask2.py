#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    original_dict = {
        1: 'один',
        2: 'два',
        3: 'три',
        4: 'четыре',
    }

    dict_items_object = original_dict.items()

    reversed_dict = {value: key for key, value in dict_items_object}

    print("Исходный словарь:")
    print(original_dict)

    print("\nНовый словарь (обратный):")
    print(reversed_dict)
