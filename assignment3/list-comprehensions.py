# Task 3: List Comprehensions Practice

import csv

employees = []

with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    employees = list(reader)

names = [
    employee[1] + " " + employee[2]
    for employee in employees[1:]
]

print(names)

names_with_e = [
    name
    for name in names
    if "e" in name.lower()
]

print(names_with_e)