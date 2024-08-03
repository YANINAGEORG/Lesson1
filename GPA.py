from typing import Any

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_alphabet = sorted(students)  # упорядочение элементов множества
print('список учеников - ', students_alphabet)


grades = [(sum(x)/len(x)) for x in grades]  # находит среднее значение каждого вложенного списка
print('ведомость средних баллов -', grades)

GPA_grades = {}
for a in range(len(students_alphabet)):
    GPA_grades[students_alphabet[a]] = grades[a]

print('средний балл каждого ученика -', GPA_grades)
