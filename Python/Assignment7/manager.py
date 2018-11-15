"""
    manager class
    an object of this class represents an employee object
    that is a manager.
    this class inherits the employee class
"""

# import Employee class that the Manager class will derive from
from employee import Employee

class Manager(Employee):
    # constructor for Manager class
    # inits the derived Employee class
    def __init__(self, first, last, social, salary, title, bonus):
        super().__init__(first, last, social, salary)
        self.title = title
        self.bonus = bonus

    def getTitle(self):
        return self.title

    def getBonus(self):
        return self.bonus

    def __str__(self):
        return "%s Title: %s and Bonus: $%i" % (super().__str__(), self.getTitle(), self.getBonus())

