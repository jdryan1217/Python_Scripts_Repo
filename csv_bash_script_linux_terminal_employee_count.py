'''
BASH COMMAND TO:Python script that achieves two tasks. First, it reads a CSV file containing a list of the employees in the organization. Second, it generates a report of the number of people in each department in a plain text file.

You need to write a Python script that reads a CSV file containing a list of the employees in the organization, counts how many people are in each department, and then generates a report using this information. The output of this script will be a plain text file.

cd data

ls

cat employees.csv

cd ~/scripts
#Create a file named generate_report.py using the following command:
nano generate_report.py



'''
#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
    # Register a custom dialect to handle leading spaces
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

    # Open the CSV file and read it using DictReader
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')

    # Create a list to hold employee dictionaries
    employee_list = []
    for data in employee_file:
        employee_list.append(dict(data))

    return employee_list


def process_data(employee_list):
    # Collect all department names
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    # Count employees per department
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data


def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ":" + str(dictionary[k]) + "\n")
        f.close()


# Test all functions
employee_list = read_employees('/home/student/data/employees.csv')
print(employee_list)

dictionary = process_data(employee_list)
print(dictionary)

write_report(dictionary, '/home/student/data/report.txt')



