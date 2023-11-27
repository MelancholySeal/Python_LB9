#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    students = []

    num_students = int(input("Введите количество студентов: "))

    for _ in range(num_students):

        student_data = {'фамилия и инициалы': input("Введите фамилию и инициалы студента: "),
                        'номер группы': int(input("Введите номер группы студента: ")),
                        'успеваемость': [float(input(f"Введите оценку {i + 1}: ")) for i in range(5)]}

        students.append(student_data)

    students.sort(key=lambda x: x['номер группы'])

    flag = False
    for student in students:
        avg_grade = sum(student['успеваемость']) / len(student['успеваемость'])
        if avg_grade > 4.0:
            print(f"Фамилия и инициалы: {student['фамилия и инициалы']}, Номер группы: {student['номер группы']}")
            flag = True

    if not flag:
        print("Нет студентов с средним баллом больше 4.0.")

