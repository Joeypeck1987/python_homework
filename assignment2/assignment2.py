import csv
import traceback
import os
import custom_module
from datetime import datetime

# task 2
def read_employees():
    employees = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)

            for index, row in enumerate(reader):
                if index == 0:
                    employees["fields"] = row
                else:
                    rows.append(row)

            employees["rows"] = rows
            return employees

    except Exception as e:
        print(f"Exception type: {type(e).__name__}")

employees = read_employees()
print(employees)

# task 3
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# task 4
def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

# task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# task 7
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

# task 8 
def employee_dict(row):
    employee = {}

    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            employee[field] = row[index]

    return employee

# task 9
def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        all_employees[employee_id] = employee_dict(row)

    return all_employees
# task 10
def get_this_value():
    return os.getenv("THISVALUE")

# task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# task 12 helper function
def read_csv_to_dict(filename):
    data = {}
    rows = []

    with open(filename, "r") as file:
        reader = csv.reader(file)

        for index, row in enumerate(reader):
            if index == 0:
                data["fields"] = row
            else:
                rows.append(tuple(row))

    data["rows"] = rows
    return data


# task 12
def read_minutes():
    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

# task 13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    return set1.union(set2)


minutes_set = create_minutes_set()

# task 14
def create_minutes_list():
    minutes_list = list(minutes_set)

    minutes_list = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        minutes_list
    ))

    return minutes_list

minutes_list = create_minutes_list()

# task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])

    sorted_list = list(map(
        lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
        minutes_list
    ))

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(minutes1["fields"])

        for row in sorted_list:
            writer.writerow(row)

    return sorted_list


write_sorted_list()