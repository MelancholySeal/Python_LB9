#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    # Исходный словарь
    original_dict = {
        1: 'один',
        2: 'два',
        3: 'три',
        4: 'четыре',
        # Добавьте другие пары ключ-значение
    }

    # Используем метод items() для получения объекта dict_items
    dict_items_object = original_dict.items()

    # Создаем новый словарь "обратный" исходному
    reversed_dict = {value: key for key, value in dict_items_object}

    # Вывод исходного и нового словарей
    print("Исходный словарь:")
    print(original_dict)

    print("\nНовый словарь (обратный):")
    print(reversed_dict)
