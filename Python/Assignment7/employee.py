"""
    employee class
    an object of this class represents one employee
    that has a first name, last name, SSN and a salary
"""
class Employee:
    # default constructor that assigns values to
    # first name, last name, SSN and salary
    def __init__(self, firstName, lastName, socialSecurityNumber, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.socialSecurityNumber = socialSecurityNumber
        self.salary = salary

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getSSN(self):
        return self.socialSecurityNumber

    def getSalary(self):
        return self.salary

    # this method accepts a float parameter
    # that is multiplied by salary and added to
    # salary variable
    def giveRaise(self, percentRaise):
        raiseAmount = self.salary * percentRaise
        self.salary += raiseAmount

    # this method returns a string value of:
    # firstname last name, makes [salary], and their SSN is [SSN]
    def __str__(self):
        return "%s %s makes $%i, and their SSN: %s" % (self.getFirstName(), self.getLastName(), self.getSalary(), self.getSSN())

