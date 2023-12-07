#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    school = {
        '1а': 12,
        '1б': 32,
        '2б': 24,
        '6а': 23,
        '7в': 30,
    }

    print("Исходный словарь:")
    print(school)

    total_students = sum(school.values())
    print("\nОбщее количество учащихся в школе:", total_students)

    school['1а'] = 20

    school['8г'] = 29

    if '2б' in school:
        del school['2б']

    print("\nИзмененный словарь:")
    print(school)

    total_students = sum(school.values())
    print("\nОбщее количество учащихся в школе:", total_students)
