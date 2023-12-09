#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Список студентов.
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            # Запросить данные о студенте.
            full_name = input("Фамилия и инициалы? ")
            group_number = input("Номер группы? ")
            grades_str = input("Успеваемость (через пробел)? ")

            # Преобразовать строки с оценками в список чисел.
            grades = [float(grade) for grade in grades_str.split()]

            # Создать словарь.
            student = {
                'full_name': full_name,
                'group_number': group_number,
                'grades': grades,
            }

            # Добавить словарь в список.
            students.append(student)

            # Отсортировать список по номеру группы.
            students.sort(key=lambda item: item.get('group_number', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 30,
                '-' * 15,
                '-' * 20
            )
            print(line)
            print(
                '| {:^30} | {:^15} | {:^20} |'.format(
                    "Ф.И.О.",
                    "Номер группы",
                    "Успеваемость"
                )
            )
            print(line)
            # Вывести данные о студентах с успеваемостью более 4.0.
            for student in students:
                average_grade = sum(student.get('grades', 0)) / len(student.get('grades', 1))
                if average_grade > 4.0:
                    print(
                        '| {:<30} | {:<15} | {:<20} |'.format(
                            student.get('full_name', ''),
                            student.get('group_number', ''),
                            ', '.join(map(str, student.get('grades', [])))
                        )
                    )
            print(line)
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}")
