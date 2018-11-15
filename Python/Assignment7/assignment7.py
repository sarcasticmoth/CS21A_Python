"""
    Vanessa Ulloa
    CS21A
    14 November 2018
    Assignment 7
"""

# import employee and manager classes
from employee import Employee
from manager import Manager

# this file is a test file to test the employee and manager classes

if __name__ == "__main__":

    companyEmployees = list()
    companyEmployees.append(Manager("Jose", "Ulloa", "987-65-4321", 20000, "Manager", 2000))
    companyEmployees.append(Manager("Vatche", "Alexan", "876-54-3210", 20000, "Manager", 2000))
    companyEmployees.append(Employee("Vanessa", "Ulloa", "234-11-0973", 15000))
    companyEmployees.append(Employee("Bob", "Wilson", "876-54-3210", 14000))
    companyEmployees.append(Employee("John", "Doe", "423-41-2341", 13000))

    # give a raise to every employee
    # print the before raise and after raise
    for e in companyEmployees:
        print(e)
        e.giveRaise(.10)
        print(e)
        print()

    print("\nTests:\n")

    # TEST: get the first name of every employee
    print("Get Employee First Names:")
    for e in companyEmployees:
        print(e.getFirstName())

    # TEST: get the last name of every employee
    print("\nGet Employee Last Names:")
    for e in companyEmployees:
        print(e.getLastName())

    # TEST: get the SSN of every employee
    print("\nGet Employee SSN:")
    for e in companyEmployees:
        print(e.getSSN())

    # TEST: get the salary of every employee
    print("\nGet Employee Salaries:")
    for e in companyEmployees:
        print(e.getSalary())
