#task 1
#test 1
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)

print(task1_data_frame)

#test 2
task1_with_salary = task1_data_frame.copy()

task1_with_salary["Salary"] = [70000, 80000, 90000]

print(task1_with_salary)

#test 3
task1_older = task1_with_salary.copy()

task1_older["Age"] = task1_older["Age"] + 1

print(task1_older)
#test 4

task1_older.to_csv("employees.csv", index=False)

#task 2
#test 1
task2_employees = pd.read_csv("employees.csv")

print(task2_employees)

#test 2
json_employees = pd.read_json("additional_employees.json")

print(json_employees)

#test 3
more_employees = pd.concat(
    [task2_employees, json_employees],
    ignore_index=True
)

print(more_employees)

#Task 3 
#test 1
first_three = more_employees.head(3)

print(first_three)

#test 2
last_two = more_employees.tail(2)

print(last_two)

#test 3

employee_shape = more_employees.shape

print(employee_shape)

more_employees.info()


#data cleaning
#test 4
dirty_data = pd.read_csv("dirty_data.csv")

print(dirty_data)

#test 5
clean_data = dirty_data.copy()

clean_data = clean_data.drop_duplicates()

print(clean_data)

#test 6
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")

print(clean_data)

#CONVERTING SALARY COLUMN
#test 7
clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")

print(clean_data)

#test 8
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())

clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())

print(clean_data)

#test 9
clean_data["Hire Date"] = pd.to_datetime(
    clean_data["Hire Date"],
    format="mixed",
    errors="coerce"
)

print(clean_data)

#test 10
clean_data["Department"] = clean_data["Department"].str.strip()
clean_data["Department"] = clean_data["Department"].str.upper()

print(clean_data)