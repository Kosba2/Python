# Homework No. FINAL  Exercise No.3
# File Name:     Employee.py
# Programmer:    Kostyantyn Shumishyn
# Date:          December 14, 2017
#
# Problem Statement: Employee Class


class Employee:

    def __init__(self, firstName, lastName, employeeID):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeID = employeeID

    @property
    def FirstName(self):
        return self.firstName

    @property
    def LastName(self):
        return self.lastName

    @property
    def EmployeeID(self):
        return self.employeeID

    def GetInfo(self):
        return str("Name: " + self.FirstName + " " + self.LastName + "\nID: " + self.EmployeeID)
