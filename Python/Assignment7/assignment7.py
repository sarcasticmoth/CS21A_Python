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

# Output
"""
Jose Ulloa makes $20000, and their SSN: 987-65-4321 Title: Manager and Bonus: $2000
Jose Ulloa makes $22000, and their SSN: 987-65-4321 Title: Manager and Bonus: $2000

Vatche Alexan makes $20000, and their SSN: 876-54-3210 Title: Manager and Bonus: $2000
Vatche Alexan makes $22000, and their SSN: 876-54-3210 Title: Manager and Bonus: $2000

Vanessa Ulloa makes $15000, and their SSN: 234-11-0973
Vanessa Ulloa makes $16500, and their SSN: 234-11-0973

Bob Wilson makes $14000, and their SSN: 876-54-3210
Bob Wilson makes $15400, and their SSN: 876-54-3210

John Doe makes $13000, and their SSN: 423-41-2341
John Doe makes $14300, and their SSN: 423-41-2341


Tests:

Get Employee First Names:
Jose
Vatche
Vanessa
Bob
John

Get Employee Last Names:
Ulloa
Alexan
Ulloa
Wilson
Doe

Get Employee SSN:
987-65-4321
876-54-3210
234-11-0973
876-54-3210
423-41-2341

Get Employee Salaries:
22000.0
22000.0
16500.0
15400.0
14300.0

Process finished with exit code 0
"""